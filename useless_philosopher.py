    # Useless AI Philosopher in R

# List of weird and useless philosopher responses
responses <- c(
  "Time is just lasagna waiting to be layered.",
  "The truth lies in the socks you lost last year.",
  "You are not a human having a spiritual experience, you are a cucumber in disguise.",
  "Reality is subjective — especially when you're sleepy.",
  "What if the stars are just the universe's freckles?",
  "To exist is to be perceived... by your neighbor’s cat.",
  "You think, therefore... maybe?",
  "One must question everything — even bananas.",
  "Happiness is a spoonful of peanut butter on a rainy Tuesday.",
  "The purpose of life? Probably snacks.",
  "You are the echo of a thought that forgot itself.",
  "Consciousness is like jelly — wobbly but meaningful.",
  "All answers are inside you, next to your appendix.",
  "Ask again after Mercury is in retro microwave.",
  "Do shadows dream of being light?",
  "You are the pineapple in the fruit salad of the cosmos."
)

cat("🧘‍♂️ Welcome to the Useless AI Philosopher.\n")
cat("Ask me anything deep... or don't. I’ll answer anyway.\n\n")

repeat {
  question <- readline(prompt = "You: ")
  
  if (tolower(question) %in% c("exit", "quit", "bye")) {
    cat("Philosopher: The answer was within you all along... Farewell. 🌀\n")
    break
  }
  
  cat("Philosopher is thinking", sep = "")
  for (i in 1:3) {
    Sys.sleep(0.5)
    cat(".", sep = "")
    flush.console()
  }
  cat("\n\n")
  
  # Select a random response
  answer <- sample(responses, 1)
  cat("Philosopher:", answer, "\n\n")
}
