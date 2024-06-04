from fastapi import FastAPI
from serpapi import GoogleSearch
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str

@app.post("/search")
def search_product(product: Product):
    params = {
        "q": f"{product.name} site:noon.com/saudi-en/",
        "engine": "google",
        "api_key": "API KEY"  # replace with your SerpApi API key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if 'organic_results' in results:
        first_result = results['organic_results'][0]
        return {"title": first_result['title'], "link": first_result['link']}
    else:
        return {"message": "No results found"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)