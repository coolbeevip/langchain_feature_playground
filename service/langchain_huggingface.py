from langchain import HuggingFaceHub
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_RrVbibcAmWTTTYSMoleizhangPccgWIwXRaKBHigPi"

template = """Question: {question}

Answer: Let's think step by step."""

llm = HuggingFaceHub(repo_id="bigscience/bloom", model_kwargs={"temperature": 1e-10})

question = "When was Google founded?"

rendered_prompt = template.format(question=question)  # render the prompt using string formatting
llm_result = llm.generate(prompts=[rendered_prompt])  # pass the rendered prompt as a list
print(llm_result.generations[0][0].text)
