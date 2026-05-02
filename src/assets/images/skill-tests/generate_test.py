import requests
import time
import os

API_KEY = "sk-lQsah9Z9K0KtbaoEP3ORRWQKf27xNQYFkvoK5ZQuiOwtNJv4"
BASE_URL = "https://toapis.com/v1"

# Three test scenarios
scenarios = [
    {
        "id": "01-baoyu-article-illustrator",
        "prompt": "A clean circular infographic showing the Agentic Loop cycle with three stages: Explore (magnifying glass), Act (hammer/tool), Validate (checkmark). Curved arrows connecting them clockwise. Style: flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose), white background, clean educational textbook aesthetic, minimal text labels only."
    },
    {
        "id": "02-document-illustrator-vector",
        "prompt": "An infographic of a T-shaped skills model. A large letter 'T' in the center. Vertical bar labeled 'Depth' with coding icons (terminal, brackets, bug). Horizontal bar labeled 'Breadth' with AI tools and community icons (robot, chat bubble, people). Intersection glows with 'Judgment + Taste'. Style: flat vector illustration, unified black outline strokes, retro-soft color palette (soft purple and teal), white background, clean educational aesthetic, minimal text."
    },
    {
        "id": "03-gpt-image-2-scientific",
        "prompt": "A flat illustration showing Docker container concept as a shipping metaphor. Left: laptop with scattered app icons in chaos. Middle: shipping container encapsulating app + runtime + dependencies. Right: another laptop opening the same container, app runs identically. Style: clean scientific educational illustration, soft blue and orange palette, white background, crisp vector lines, textbook diagram aesthetic, minimal labels."
    }
]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

output_dir = "e:/00llm-wiki/01Projects/给零基础小白准备的AI时代优雅编程/src/assets/images/skill-tests"

for scenario in scenarios:
    print(f"\n=== Generating: {scenario['id']} ===")

    # Step 1: Submit generation request
    payload = {
        "model": "gpt-image-2",
        "prompt": scenario["prompt"],
        "size": "1536x1024",
        "n": 1
    }

    resp = requests.post(
        f"{BASE_URL}/images/generations",
        headers=headers,
        json=payload,
        timeout=60
    )
    resp.raise_for_status()
    data = resp.json()
    print(f"Submit response: {data}")

    task_id = data.get("id") or data.get("task_id")
    if not task_id:
        print(f"ERROR: No task_id returned for {scenario['id']}")
        continue

    # Step 2: Poll until completed
    max_retries = 60
    for i in range(max_retries):
        time.sleep(5)
        poll_resp = requests.get(
            f"{BASE_URL}/images/generations/{task_id}",
            headers=headers,
            timeout=30
        )
        poll_resp.raise_for_status()
        poll_data = poll_resp.json()

        status = poll_data.get("status", "unknown")
        print(f"  Poll {i+1}: status={status}")

        if status == "completed":
            # Download image
            image_url = None
            result = poll_data.get("result", {})
            if "data" in result and len(result["data"]) > 0:
                image_url = result["data"][0].get("url")
            elif "data" in poll_data and len(poll_data["data"]) > 0:
                image_url = poll_data["data"][0].get("url")
            elif "output" in poll_data:
                image_url = poll_data["output"].get("url")
            elif "url" in poll_data:
                image_url = poll_data["url"]

            if image_url:
                img_resp = requests.get(image_url, timeout=60)
                img_resp.raise_for_status()
                out_path = os.path.join(output_dir, f"{scenario['id']}.png")
                with open(out_path, "wb") as f:
                    f.write(img_resp.content)
                print(f"  SAVED: {out_path}")
            else:
                print(f"  ERROR: No image URL found in completed response: {poll_data}")
            break
        elif status in ("failed", "error", "cancelled"):
            print(f"  ERROR: Task failed with status={status}, data={poll_data}")
            break
    else:
        print(f"  ERROR: Polling timed out for {scenario['id']}")

print("\n=== All generations complete ===")
