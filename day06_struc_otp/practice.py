import json
import time
from pydantic import BaseModel, Field, ValidationError

# ==========================================================
# 1. डेटा स्कीमा परिभाषित करना (Define Data Structure)
# ==========================================================
class Resume(BaseModel):
    name: str = Field(min_length=1)
    role: str = Field(min_length=1)
    experience: int = Field(ge=0)
    skills: list[str]


# ==========================================================
# 2. सिम्युलेटेड AI रिस्पांस (Simulated LLM Responses)
# ==========================================================
# यहाँ केवल 2 रिस्पांस हैं, तीसरा प्रयास खाली/फेल माना जाएगा
responses = [
    """
    {
        "name": "Rahul Sharma",
        "role": "Python Developer",
        "experience": 5,
        "skills": ["Python", "SQL"]
    }
    """,
    """
    {
        "name": "Rahul Sharma",
        "role": "Python Developer",
        "experience": 2,
        "skills": ["Python", "SQL", "FastAPI"]
    }
    """
]


# ==========================================================
# 3. रीट्राय कॉन्फ़िगरेशन (Retry Configuration)
# ==========================================================
MAX_RETRIES = 3


# ==========================================================
# 4. AI रिस्पांस को प्रोसेस और वैलिडेट करना
# ==========================================================
for attempt in range(1, MAX_RETRIES + 1):
    try:
        print(f"\nAttempt: {attempt}")
        
        # IndexError से बचने के लिए सुरक्षा जांच (Safe Index Check)
        if (attempt - 1) < len(responses):
            raw_response = responses[attempt - 1]
        else:
            # यदि 3रे प्रयास में कोई डेटा नहीं है, तो खाली JSON भेजें जो फेल हो जाएगा
            raw_response = "{}" 
        
        # Pydantic की मदद से JSON वैलिडेट करना
        resume = Resume.model_validate_json(raw_response)
        
        print("Validation Successful!")
        print(resume.model_dump_json(indent=4))
        
        # सफलता मिलने पर लूप से बाहर निकलें
        break
        
    except ValidationError as error:
        print("Validation Failed!")
        print(f"Error Details:\n{error}")
        
        if attempt == MAX_RETRIES:
            print("\n[Alert] Maximum retries (3) reached. All responses failed!")
        else:
            print("Retrying with next response...")
            time.sleep(1)
