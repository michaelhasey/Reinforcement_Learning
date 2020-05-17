import main
import gym
gym.logger.set_level(40)  # Explicitly specify dtype as float32

env = gym.make("CartPole-v1")
obs = env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample()  # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)

    if done:
        obs = env.reset()
env.close()
