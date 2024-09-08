# ATS_RESUME_SCANNER


THIS PROJECT CAN BE DONE BY 2 DIFFERENT WAYS

TECHNIQUE 1: 
upload the JD AS TEXT & also upload the pdf => convert the pdf into image using(pdf2img) => the use encoding and decoding technique 
which gather the information from the image and convert that in to an bytes => send that information into generativeAI like huggingface, 
openAI, gemini and get response back from that models

TECHNIQUE2:
Upload the JD AS TEXT & also upload the pdf  => directly extract the information(text) from the pdf using(pypdf2) => & pass the the 
info to generativeAI like huggingface, openAI, gemini  => and get the response back from that models for that make a suitable prompt
to get an accurate result
