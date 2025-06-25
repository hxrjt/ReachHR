import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GOOGLE_CX=os.getenv("GOOGLE_CX")

def get_company_name(company_name):
    #Returns the official website of company
    
    query=f"{company_name} Official Site"
    url=f"https://www.googleapis.com/customsearch/v1"
    param={
        "key":GOOGLE_API_KEY,
        "cx":GOOGLE_CX,
        "q":query
    }
    
    try:
        response=requests.get(url, params=param)
        data=response.json()
        results=response.json().get("items",[])
        if results:
            for item in results:
                link=item["link"]
                if company_name.lower().split()[0] in link.lower():
                    return link
            return results[0]["link"]
        return "No Website Found For This Company"
    
    except Exception as e:
        return f"Error:{str(e)}"

def get_hr_profiles(company_name,location,max_result=10):
    #returns hr profiles according to location
    
    query=f"HR or Recruiters at {company_name} in {location} site:linkedin.com/in"
    url=f"https://www.googleapis.com/customsearch/v1"
    param={
        "key":GOOGLE_API_KEY,
        "cx":GOOGLE_CX,
        "q":query,
        "num":max_result
    }
    
    try:
        response=requests.get(url,params=param)
        results=response.json().get("items",[])
        profiles=[]
        
        for item in results:
            title=item["title"]
            snippet=item.get("snippet","")
            if company_name.lower() in title.lower() or (company_name.lower() in snippet.lower() and location.lower() in snippet.lower()):
                profiles.append({
                    "name":item["title"],
                    "link":item["link"],
                    "snippet":item.get("snippet","")
                })
        # return profiles if profiles else[{"name": "No HRs found in this location", "link": "", "snippet": ""}]
        return profiles
    except Exception as e:
        return [{"name": "Error", "link": "", "snippet": str(e)}]
    
