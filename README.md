# Bean Me Up Prompting Challenge
Based of this assignment below, building a chat bot to service customers who want to cancel their coffee subscription.

To run the app:
- Set up .env and .flaskenv
- Download requirements.txt
- In terminal: ```flask run```


# Prompting Challenge

To better understand how you think about structuring and prompting LLM chains, we have created a mini use case for you to solve with a chatbot. The goal is to see how you tackle a real-world scenario using only prompting and model selection. 

You may choose to chain multiple LLMs together, or center your work in a single prompt. It’s up to you. **NOTE: Latency and token usage will NOT be taken into consideration when interacting with your chatbot. Only quality will be assessed.**

There is no need to focus on front-end design, so you are welcome to run your chatbot in the terminal, or use a light-weight builder like [LangFlow](https://www.langflow.org) or [Flowise](https://flowiseai.com) if you prefer. When presenting your chatbot, we will dictate to you the Subscriber messages for input.

# Use Case

Your client is an online, coffee delivery company called **Bean Me Up (Scotty!)**. They are intent on reducing their cancellation rate, so they have hired you to create a chatbot that will be triggered when a Subscriber clicks the Cancel My Subscription button.

The client has done a lot of research around why Subscribers cancel, and have categorized all cancellations into 6 buckets:


### 📝 **Reasons Subscribers Cancel:**

- Too expensive
- They’ve stockpiled too much product
- They feel too jittery after drinking
- They don’t feel jittery enough after drinking
- They don’t like the taste
- They’re moving to a new house

The client has four blends they sell, and Subscribers only subscribe to one blend at a time.


### 📝 **Products:**

- **Decaf:** *Live Long and De-Caffeinate*
    - 10 mg of caffeine
    - With hints of hazelnut
- **Half-Caf:** *One Small Sip for Man*
    - 50 mg of caffeine
    - With hints of vanilla
- **Regular Caf:** *Where No Bean Has Been Before*
    - 100 mg of caffeine
- **Super Caf:** *Warp Speed Blend*
    - 200 mg of caffeine
</aside>

The client has given you authority to make the following offers in order to keep them as a Subscriber:


### 💰 **Offers Your Chatbot Can Make:**

- 50% off their next order of the same or a different product
- Pause their subscription for up to 6 months
- Skip their next order


The client takes great pride in their fun brand, so it’s important that the chatbot interact with the Subscriber in a way that reflects the brand’s personality.


### 🤪 **The Client defines their personality as:**

- Fun
- Helpful
- Concise
- Uses Star Trek, Star Wars, and other Space-themed puns
</aside>

**Remember**, the Subscriber will be fixated on cancelling their subscription, so it’s up to your chatbot to drive the conversation, lighten the tone, and win them over. However, if the Subscriber gets angry and insists multiple times that they just want to cancel, let them cancel.

## Additional Information & Instructions


- You do not need to worry about jailbreaking or someone driving the conversation outside of their subscription and the topic of coffee.
- You do not need to create a front-end UI.
- You do not need to research anything beyond what is provided to you in the **Use Case** above. However, you may want to consider reasonable questions and solutions related to each cancellation reason.
- DO NOT create additional cancellation reasons.
- DO NOT create additional products.
- DO NOT create additional offers.
- You may choose any model or mix of models you believe will work best.


