# Tron AI Game  

## Overview  
This project is a Tron game developed as a guided project through the **MSU AI Club**. The game allows players to compete against an AI opponent trained using reinforcement learning. The project was built using **Python** and **pygame**, incorporating AI decision-making to create a competitive gameplay experience.  

## Features  
- **Classic Tron Gameplay**: Navigate a grid-based arena while avoiding walls and trails.  
- **AI Opponent**: The AI is trained using reinforcement learning to make strategic decisions.  
- **Training Mode**: Train the AI using reinforcement learning.  
- **Player vs AI Mode**: Play against the AI to test its strategies.  

## Challenges and Custom AI Development  
During **Week 6**, I encountered challenges when attempting to train an AI using reinforcement learning beyond the provided script. My computer hardware had limitations that prevented effective RL training, making it difficult to achieve a competitive AI opponent.  

To overcome this, I decided to create my own AI bot that does not rely on RL but instead follows a **rule-based approach** with smarter decision-making. The AI considers the player's position and avoids dead ends while attempting to cut off the player strategically.  

Here’s a simplified version of the AI’s logic:  
- It evaluates possible moves and avoids its own trail.  
- It prioritizes paths that keep it from crashing.  
- If multiple safe moves exist, it moves towards the player to force them into a disadvantageous position.  

This approach allowed me to create a functional AI opponent that could compete effectively without requiring extensive training resources.  

## Project Timeline  
This project followed a structured development process over six weeks with resources from the **MSU AI Club**:  
- [Week 1: Game Setup](https://www.msuaiclub.com/posts/ea0f1533-99e7-474b-b701-917e901ca08c)  
- [Week 2: Basic AI Implementation](https://www.msuaiclub.com/posts/23ded9a9-5a5d-4d54-898a-dfa4ef2519cc)  
- [Week 3: AI Strategy Improvements](https://www.msuaiclub.com/posts/d53d3786-a9d5-45dd-9390-eb69ad085788)  
- [Week 4: Enhancing AI Decision-Making](https://www.msuaiclub.com/posts/ff91348d-b169-424a-85a1-96fed6b8f17a)  
- [Week 5: Testing and Optimization](https://www.msuaiclub.com/posts/cae3fb7a-a36d-4869-af34-6b0e13ef9d23)  
- [Week 6: Finalizing and Debugging](https://www.msuaiclub.com/posts/b3504837-8d9f-462a-9a5d-9a614e14b523)  

## Contributions  
This project was developed as part of a guided project at **MSU AI Club**, where members learned reinforcement learning concepts and applied them in game development.  


