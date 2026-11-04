import json
from pydantic import BaseModel, Field, ValidationError

# ==========================================
# --- भाग 1: JSON dump का उदाहरण ---
# ==========================================
student = {
    "name": "Rahul",
    "age": 25,
    "city": "Delhi"
}

# डिक्शनरी को सुंदर फॉर्मेट में JSON स्ट्रिंग में बदलना
json_data = json.dumps(student, indent=4)

print("--- JSON Output ---")
print(json_data)


# ==========================================
# --- भाग 2: Pydantic Model का उदाहरण ---
# ==========================================

# Pydantic की मदद से डेटा स्कीमा (Schema) परिभाषित करना
class Resume(BaseModel):
    name: str
    role: str
    experience: int = Field(ge=0)  # अनुभव 0 या उससे ज़्यादा होना चाहिए
    skills: list[str]

# Try-Except ब्लॉक की मदद से Validation को सुरक्षित तरीके से रन करना
try:
    # Pydantic मॉडल का ऑब्जेक्ट (Instance) बनाना
    resume_data = Resume(
        name="Rahul Sharma",
        role="Python Developer",
        experience=-2,            # यदि आप यहाँ -2 लिखेंगे तो ValidationError ट्रिगर होगा
        skills=["Python", "SQL", "FastAPI"]
    )
    
    print("--- Pydantic Model Output ---")
    print(resume_data)
    
except ValidationError as error:
    print("--- Validation Error Caught ---")
    print(error)
