from personality_trip_recommender.crew import PersonalityTripRecommenderCrew

def kickoff(inputs: dict):
    crew = PersonalityTripRecommenderCrew()
    crew.kickoff(inputs=inputs)

if __name__ == "__main__":
    user_input = {
        "personality_traits": "adventurous, introverted, budget-conscious"
    }
    kickoff(inputs=user_input)
