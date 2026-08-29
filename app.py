import streamlit as st
import os
from src.retriever import retrieve_documents
from src.generator import generate_answer


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Almamlaka TV RAG Chatbot",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto"
)


# --------------------------------------------------
# Custom Styling - Loading CSS only once
# --------------------------------------------------

def load_css():
    """Load CSS only once to improve performance"""
    if "css_loaded" not in st.session_state:
        st.markdown(
            """
            <style>
            /* Main styles - optimized for speed */
            .stApp {
                background: #f5f7fa;
            }
            
            .main-title {
                text-align: center;
                font-size: 32px;
                font-weight: 700;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 5px;
                padding: 15px 0 5px 0;
            }

            .subtitle {
                text-align: center;
                color: #6c757d;
                margin-bottom: 25px;
                font-size: 15px;
            }

            /* User messages */
            [data-testid="stChatMessage"][data-role="user"] {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                color: white !important;
                border-radius: 18px 18px 4px 18px !important;
                padding: 12px 16px !important;
                margin-bottom: 10px !important;
                box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2) !important;
            }

            [data-testid="stChatMessage"][data-role="user"] p {
                color: white !important;
                margin: 0 !important;
            }

            /* Assistant messages */
            [data-testid="stChatMessage"][data-role="assistant"] {
                background: white !important;
                border: 1px solid #e9ecef !important;
                border-radius: 18px 18px 18px 4px !important;
                padding: 12px 16px !important;
                margin-bottom: 10px !important;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
            }

            [data-testid="stChatMessage"][data-role="assistant"] p {
                margin: 0 0 8px 0 !important;
                color: #2d3436 !important;
            }

            /* Buttons */
            .stButton button {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                color: white !important;
                border: none !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
                padding: 8px 16px !important;
                transition: all 0.2s ease !important;
                width: 100% !important;
            }

            .stButton button:hover {
                transform: translateY(-1px);
                box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
            }

            .stButton button:active {
                transform: translateY(0px);
            }

            /* Chat input */
            .stChatInput {
                padding-bottom: 15px !important;
            }

            .stChatInput input {
                border-radius: 25px !important;
                border: 2px solid #e9ecef !important;
                padding: 10px 20px !important;
                background: white !important;
                font-size: 14px !important;
                transition: all 0.2s ease !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
            }

            .stChatInput input:focus {
                border-color: #667eea !important;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
            }

            .stChatInput input::placeholder {
                color: #adb5bd !important;
            }

            /* Sidebar */
            .css-1d391kg {
                background: #ffffff !important;
                border-right: 1px solid #e9ecef !important;
            }

            /* Expanders - Sources */
            .streamlit-expanderHeader {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                color: white !important;
                border-radius: 6px !important;
                font-weight: 600 !important;
                font-size: 14px !important;
                padding: 8px 12px !important;
                border: none !important;
            }

            .streamlit-expanderHeader:hover {
                opacity: 0.9 !important;
            }

            .streamlit-expanderContent {
                background: white !important;
                border-radius: 0 0 6px 6px !important;
                border: 1px solid #e9ecef !important;
                border-top: none !important;
                padding: 8px 12px !important;
            }

            /* Source items */
            .source-item {
                display: flex;
                align-items: center;
                gap: 8px;
                padding: 6px 10px;
                background: #f8f9fa;
                border-radius: 6px;
                margin-bottom: 4px;
                font-size: 13px;
                border-left: 3px solid #667eea;
            }

            .source-item:hover {
                background: #e9ecef;
            }

            .source-item .icon {
                font-size: 16px;
            }

            .source-item .file-name {
                font-weight: 600;
                color: #2d3436;
            }

            .source-item .page-num {
                color: #6c757d;
                font-size: 12px;
            }

            /* Welcome box */
            .welcome-box {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 16px 20px;
                border-radius: 12px;
                margin-bottom: 15px;
                box-shadow: 0 2px 12px rgba(102, 126, 234, 0.2);
                line-height: 1.6;
            }

            .welcome-box h3 {
                margin: 0 0 8px 0;
                font-size: 18px;
            }

            .welcome-box p {
                margin: 4px 0;
                opacity: 0.95;
            }

            /* Footer */
            .footer {
                text-align: center;
                padding: 20px 20px 10px 20px;
                color: #6c757d;
                font-size: 12px;
                margin-top: 30px;
                border-top: 1px solid #e9ecef;
            }

            .footer strong {
                color: #667eea;
            }

            /* Metrics in sidebar */
            .metric-box {
                background: white;
                padding: 8px;
                border-radius: 8px;
                text-align: center;
                border: 1px solid #e9ecef;
            }

            .metric-value {
                font-size: 22px;
                font-weight: 700;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .metric-label {
                color: #6c757d;
                font-size: 11px;
                margin-top: 2px;
            }

            /* Divider */
            hr {
                margin: 15px 0 !important;
                border: none !important;
                border-top: 2px solid #e9ecef !important;
                opacity: 0.5;
            }

            /* Toast messages */
            .stToast {
                border-radius: 10px !important;
                background: white !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
                border-left: 4px solid #667eea !important;
            }

            /* Spinner */
            .stSpinner {
                text-align: center !important;
            }

            .stSpinner > div {
                color: #667eea !important;
            }

            /* Responsive */
            @media (max-width: 768px) {
                .main-title {
                    font-size: 24px;
                }
                .subtitle {
                    font-size: 13px;
                }
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.session_state.css_loaded = True

# Load CSS once
load_css()


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown('<div class="main-title">📚 Almamlaka TV RAG Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask questions about the Almamlaka TV Digital Expansion Initiative</div>', unsafe_allow_html=True)


# --------------------------------------------------
# Initialize Chat History
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Sidebar - Optimized
# --------------------------------------------------

with st.sidebar:
    
    st.markdown("### ⚙️ Settings")
    st.caption("Ask about Almamlaka TV Digital Expansion")
    
    # Quick stats
    total_msgs = len(st.session_state.messages)
    user_msgs = sum(1 for m in st.session_state.messages if m["role"] == "user")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{total_msgs}</div>
                <div class="metric-label">💬 Total</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{user_msgs}</div>
                <div class="metric-label">👤 You</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True, type="primary"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # About section - simple
    with st.expander("ℹ️ About", expanded=False):
        st.caption("""
        **RAG Chatbot** using Almamlaka TV documents.
        
        🔍 Retrieves relevant content  
        🤖 Generates answers with AI  
        📚 Shows sources for transparency
        """)


# --------------------------------------------------
# Display Welcome Message
# --------------------------------------------------

if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(
            """
            <div class="welcome-box">
                <h3>👋 Welcome to Almamlaka TV Assistant!</h3>
                <p>I can help you with questions about the <b>Digital Expansion Initiative</b>.</p>
                <p style="margin-top: 8px; opacity: 0.9;">
                    <b>Try asking:</b><br>
                    📌 What are the goals of the digital expansion?<br>
                    📌 How will new technology be implemented?<br>
                    📌 What is the project timeline?
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        if message["role"] == "assistant":
            sources = message.get("sources", [])
            if sources:
                with st.expander("📚 Sources"):
                    for source in sources:
                        icon = source.get("icon", "📄")
                        st.markdown(
                            f"""
                            <div class="source-item">
                                <span class="icon">{icon}</span>
                                <span class="file-name">{source['file']}</span>
                                <span class="page-num">— Page {source['page']}</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

query = st.chat_input("💬 Ask a question about the documents...")


# --------------------------------------------------
# Process Question
# --------------------------------------------------

if query:
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": query})
    
    with st.chat_message("user"):
        st.markdown(query)
    
    # Generate Answer
    with st.chat_message("assistant"):
        
        # Use simple spinner for better performance
        with st.spinner("🔍 Searching the documents..."):
            
            # Retrieve relevant documents
            results = retrieve_documents(query, top_k=3)
            documents = results["documents"][0]
            metadatas = results["metadatas"][0]
            context = "\n\n".join(documents)
            
            # Generate answer
            answer = generate_answer(query, context)
        
        # Display answer
        st.markdown(answer)
        
        # Build Sources with icons
        file_icons = {
            '.pdf': '📄',
            '.docx': '📝',
            '.txt': '📃',
            '.pptx': '📊',
            '.xlsx': '📈',
            '.csv': '📊',
        }
        
        sources = []
        for metadata in metadatas:
            source_path = metadata["source"]
            file_name = source_path.split("/")[-1].split("\\")[-1]
            
            # Get icon based on file extension
            ext = os.path.splitext(file_name)[1].lower()
            icon = file_icons.get(ext, '📎')
            
            source = {
                "file": file_name,
                "page": metadata.get("page", "N/A"),
                "icon": icon
            }
            
            # Avoid duplicates
            if not any(s["file"] == source["file"] and s["page"] == source["page"] for s in sources):
                sources.append(source)
        
        # Display Sources
        if sources:
            with st.expander("📚 Sources"):
                for source in sources:
                    st.markdown(
                        f"""
                        <div class="source-item">
                            <span class="icon">{source['icon']}</span>
                            <span class="file-name">{source['file']}</span>
                            <span class="page-num">— Page {source['page']}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        
        # Feedback buttons - simple
        col1, col2, col3 = st.columns([1, 1, 6])
        with col1:
            if st.button("👍 Helpful", key=f"helpful_{len(st.session_state.messages)}"):
                st.toast("❤️ Thanks for your feedback!", icon="✨")
        with col2:
            if st.button("👎 Not Helpful", key=f"unhelpful_{len(st.session_state.messages)}"):
                st.toast("🙏 We'll improve! Thanks for letting us know.", icon="📝")
    
    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        🔍 Powered by <strong>RAG</strong> · Almamlaka TV Digital Expansion Initiative
        <br>
        <span style="font-size: 11px; color: #adb5bd;">
            Built with ❤️ using Streamlit
        </span>
    </div>
    """,
    unsafe_allow_html=True
)