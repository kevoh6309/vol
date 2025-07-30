# OpenRouter API Setup Guide

## 🚀 **Quick Setup**

### 1. **Get Your OpenRouter API Key**
1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Sign up for a free account
3. Navigate to your API keys section
4. Create a new API key
5. Copy the API key (starts with `sk-or-`)

### 2. **Set Environment Variable**
```bash
# On Windows (PowerShell)
$env:OPENROUTER_API_KEY="sk-or-your-api-key-here"

# On Windows (Command Prompt)
set OPENROUTER_API_KEY=sk-or-your-api-key-here

# On Linux/Mac
export OPENROUTER_API_KEY="sk-or-your-api-key-here"
```

### 3. **Create .env File (Recommended)**
Create a `.env` file in your project root:
```env
OPENROUTER_API_KEY=sk-or-your-api-key-here
OPENROUTER_API_URL=https://openrouter.ai/api/v1/chat/completions
```

## 🤖 **AI Models Available**

The chatbot is configured to use **Claude 3.5 Sonnet** by default, but you can easily switch to other models:

### **Recommended Models**
- `anthropic/claude-3.5-sonnet` (Current default)
- `openai/gpt-4o`
- `google/gemini-pro`
- `meta-llama/llama-3.1-8b-instruct`

### **Change Model**
Edit `vol/app.py` line 667:
```python
'model': 'anthropic/claude-3.5-sonnet',  # Change this line
```

## 💰 **Pricing**

OpenRouter offers competitive pricing:
- **Free Tier**: $5 credit monthly
- **Pay-as-you-go**: Very affordable rates
- **No monthly fees**: Only pay for what you use

## 🔧 **Configuration Options**

### **Customize AI Behavior**
Edit the system prompt in `vol/app.py`:
```python
'content': 'You are a helpful career assistant specializing in resume writing, interview preparation, and career advice. Provide practical, actionable advice with specific examples when possible.'
```

### **Adjust Response Length**
```python
'max_tokens': 500,  # Increase for longer responses
'temperature': 0.7,  # Lower for more focused responses
```

## 🧪 **Testing**

Test your OpenRouter integration:
```bash
python test_chatbot.py
```

You should see:
```
🎉 Chatbot is fully functional!
✅ Basic responses working
✅ Keyword recognition working
```

## 🔒 **Security**

- API keys are stored in environment variables
- Never commit API keys to version control
- Use `.env` files for local development
- Use secure environment variables in production

## 📊 **Monitoring**

Monitor your API usage:
1. Visit [OpenRouter Dashboard](https://openrouter.ai/keys)
2. Check usage statistics
3. Monitor costs and limits

## 🆘 **Troubleshooting**

### **Common Issues**

1. **"API key not found"**
   - Verify environment variable is set
   - Restart your Flask application
   - Check for typos in the API key

2. **"Rate limit exceeded"**
   - Check your OpenRouter usage
   - Consider upgrading your plan
   - Implement request caching

3. **"Model not available"**
   - Verify model name is correct
   - Check if model requires special access
   - Try a different model

### **Fallback System**

The application has a robust fallback system:
1. **OpenRouter AI** (Primary)
2. **Gemini AI** (Secondary)
3. **Rule-based responses** (Final fallback)

## 🎯 **Next Steps**

1. **Set your API key** using the instructions above
2. **Test the chatbot** with career questions
3. **Customize the prompts** for your specific needs
4. **Monitor usage** to optimize costs
5. **Consider caching** for frequently asked questions

## 📞 **Support**

- **OpenRouter Support**: [docs.openrouter.ai](https://docs.openrouter.ai)
- **API Documentation**: [openrouter.ai/api](https://openrouter.ai/api)
- **Community**: [Discord](https://discord.gg/openrouter)

---

**Status**: ✅ **Ready to use with OpenRouter integration!** 