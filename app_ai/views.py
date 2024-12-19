from django.http import HttpResponse
from django.shortcuts import render
from huggingface_hub import InferenceClient
from PIL import Image
import io
import base64
from django.conf import settings

# Replace with your Hugging Face model and token
MODEL_ID = "fofr/flux-handwriting"
HUGGINGFACE_TOKEN = settings.HUGGINGFACE_TOKEN

# Initialize the InferenceClient
client = InferenceClient(MODEL_ID, token=HUGGINGFACE_TOKEN)


def generate_handwriting(request):
    if request.method == "POST":
        text = request.POST.get("text")
        style = request.POST.get("style")
        ink_color = request.POST.get("ink_color")
        paper_type = request.POST.get("paper_type")

        if not text or not style or not ink_color or not paper_type:
            error_message = "<div class='text-red-500'>Please provide all required inputs: text, style, ink color, and paper type.</div>"
            return HttpResponse(error_message, status=400)

        try:
            # Build the AI model prompt
            prompt = f'HWRIT {style} handwriting saying "{text}", {ink_color} ink on {paper_type}'
            print(prompt)
            print("Generating handwriting...")
            image = client.text_to_image(prompt)
            print("Generation completed!")

            # Validate image dimensions
            if image.width == 0 or image.height == 0:
                error_message = "<div class='text-red-500'>Generated image dimensions are invalid.</div>"
                return HttpResponse(error_message, status=502)

            # Save the image to an in-memory file
            img_io = io.BytesIO()
            image.save(img_io, "PNG")
            img_io.seek(0)
            image_data = base64.b64encode(img_io.read()).decode("utf-8")

            # Create the HTML response with the generated image
            html_response = f"""
            <div>
                <p class="text-cyber-accent/80 italic mb-2">Generated Text: {text}</p>
                <img 
                    src="data:image/png;base64,{image_data}" 
                    alt="Generated Handwriting" 
                    class="w-full rounded-lg border-2 border-cyber-accent/30 shadow-cyber-glow"
                />
                <div class="flex justify-center space-x-4 mt-4">
                    <a
                        href="data:image/png;base64,{image_data}"
                        download="generated_handwriting.png"
                        class="bg-gradient-to-r from-cyber-accent to-cyber-secondary text-cyber-bg px-6 py-3 rounded-lg hover:opacity-90 transition-all inline-flex items-center space-x-2"
                    >
                        Download Handwriting
                    </a>
                </div>
            </div>
            """
            return HttpResponse(html_response)

        except Exception as e:
            print("error", e)
            error_message = f"<div class='text-red-500'>Error generating handwriting: {str(e)}</div>"
            return HttpResponse(error_message, status=500)

    return render(request, "generate_handwriting.html")
