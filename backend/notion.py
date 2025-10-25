from notion_client import Client as NotionClient, APIResponseError
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")

notion = NotionClient(auth=NOTION_TOKEN)

def search_notion_pages(query, page_size):
  mcp_call_details = {"query": query, "page_size": page_size}

  try:
    response = notion.search(query = query, page_size = page_size)
    
    results = response.get("results", [])

    parsed_results = []
    for res in results:
      page_id = res.get("id")

      title_property = res.get("properties", {}).get("title", {})
      page_title = "Untitled"
      if title_property.get("type") == "title":
        page_title = title_property.get("title", [{}])[0].get("plain_text", "Untitled")

      elif title_property.get("type") == "rich_text":
        page_title = title_property.get("rich_text", [{}])[0].get("plain_text", "Untitled")
      
      url = res.get("url", "#")
      if page_id and page_title:
        parsed_results.append({"id": page_id, "title": page_title, "url": url})
    return parsed_results
  
  except APIResponseError as e:
    print("API error dawg", e)
    return None
  
  except Exception as e:
    print("Some other error dawg", e)
    return None
  
def extract_text_from_blocks(blocks):
  text = []
  for block in blocks:
    block_type = block.get("type")
    if block_type and block_type in block and "rich_text" in block[block_type]:
      for segment in block[block_type]["rich_text"]:
        text.append(segment.get("plain_text", ""))
  
  return text

def get_notion_page_text(page_id):
  next_cursor = None
  all_blocks = []
  try:
    while True:
      response = notion.blocks.children.list(
        block_id=page_id,
        start_cursor=next_cursor
      )
      results = response.get("results", [])
      all_blocks.extend(results)
      next_cursor = response.get("next_cursor")
      if not response.get("has_more") or not next_cursor:
        break

    page_text = extract_text_from_blocks(all_blocks)
    text_preview = (page_text[:100] + '...') if len(page_text) > 100 else page_text

    return page_text

  except APIResponseError as e:
    return None
  except Exception as e:
    return None
  
# testing this

if __name__ == "__main__":
  search_query = "static analysis"
  pages = search_notion_pages(query = search_query, page_size=5)
  result = []
  for i in range(len(pages)):
    result.append(get_notion_page_text(pages[i].get("id")))
  print(result)