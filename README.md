# OpenAI o3-Pro Background Mode Demo

A Streamlit application that leverages OpenAI's o3-Pro model with background processing to generate extremely long responses (up to 200k tokens context window).

## Overview

This application addresses the limitation of ChatGPT Pro's ~5k token output limit by using the OpenAI API directly with o3-Pro model in background mode. Unlike the retired o1-pro (which supported ~80k tokens), this solution can handle the full 200k token context window that o3-Pro supports.

## Features

- **Full Context Window**: Supports up to 200k tokens input/output
- **Background Processing**: Uses OpenAI's background mode for long-running tasks
- **Real-time Polling**: Automatically polls for completion status
- **Large Text Areas**: Optimized UI for handling very long text inputs and outputs
- **Error Handling**: Comprehensive error handling for API failures
- **Flexible API Key Management**: Supports both environment variables and Streamlit secrets

## Why This Solution?

- **ChatGPT Pro**: Limited to ~5k tokens output
- **Retired o1-pro**: Previously supported ~80k tokens (no longer available)
- **Claude Opus 4**: Insufficient for massive responses
- **Gemini 2.5 Pro**: Doesn't meet the long-response requirements
- **Manus Pro**: High-effort mode recently retired
- **OpenAI API o3-Pro**: Currently the best solution for maximum response length

## Prerequisites

- Python 3.7+
- OpenAI API key with o3-Pro access
- Streamlit

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd long-response-ai
```

2. Install required dependencies:

```bash
pip install streamlit requests
```

3. Set up your OpenAI API key using one of these methods:

   **Option A: Environment Variable**

   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

   **Option B: Streamlit Secrets**
   Create `.streamlit/secrets.toml`:

   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```

## Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. Open your browser to the provided URL (typically `http://localhost:8501`)

3. Enter your prompt in the text area (supports very long inputs)

4. Click "Generate Response" to start the background task

5. The app will:
   - Start a background task with OpenAI
   - Display the task ID
   - Poll for completion every 2 seconds
   - Display the full response once completed

## API Endpoints Used

- **Start Background Task**: `POST https://api.openai.com/v1/responses`
- **Poll Status**: `GET https://api.openai.com/v1/responses/{response_id}`

## Configuration

The application uses the following OpenAI API configuration:

- **Model**: `o3-pro`
- **Background Mode**: Enabled for long-running tasks
- **Headers**: Includes `OpenAI-Beta: background` for beta feature access
- **Polling Interval**: 2 seconds

## Response Status Flow

1. **queued**: Task is waiting to be processed
2. **in_progress**: Model is actively generating the response
3. **completed**: Response is ready and displayed
4. **error**: Something went wrong (handled with error messages)

## Limitations & Considerations

- **API Costs**: o3-Pro is expensive, especially for long responses
- **Processing Time**: Background tasks can take several minutes for complex prompts
- **Rate Limits**: Subject to OpenAI's API rate limits
- **Beta Feature**: Background mode is currently in beta

## Troubleshooting

### Common Issues

1. **"API key missing!" error**

   - Ensure your API key is properly set via environment variable or Streamlit secrets

2. **HTTP 401 Unauthorized**

   - Verify your API key is valid and has o3-Pro access

3. **HTTP 429 Rate Limited**

   - You've exceeded API rate limits, wait and try again

4. **Long wait times**
   - This is normal for complex prompts; the app will continue polling automatically

### Error Messages

The app provides detailed error messages including:

- HTTP status codes
- API response details
- Task status information

## File Structure

```
long-response-ai/
├── app.py              # Main Streamlit application
├── README.md           # This file
└── .streamlit/
    └── secrets.toml    # API key configuration (optional)
```

## Contributing

Feel free to submit issues and enhancement requests!

## Acknowledgments

- Built for users who need maximum response length from AI models
- Utilizes OpenAI's cutting-edge o3-Pro model
- Designed to overcome the limitations of web-based AI interfaces
