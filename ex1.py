# Chapter 5: Fire Scenario Decision Code Example - Supporting Negative Weights and Correlations
# Focused on Weight-Calculative AI Decision Process in Fire Emergencies

class WeightCalculativeAI:
    def __init__(self, relation_library, weight_library, probability_library):
        """
        Initialize Weight-Calculative AI
        """
        self.relation_library = relation_library
        self.weight_library = weight_library
        self.probability_library = probability_library
        self.activated_atoms = set()
        self.central_workspace = []
        
    def pointing_operation(self, source_atom):
        """
        Pointing Operation: Activate related logical atoms
        """
        activated = set()
        if source_atom in self.relation_library:
            for target_atom in self.relation_library[source_atom]:
                activated.add(target_atom)
                # Recursively activate related atoms
                activated.update(self.pointing_operation(target_atom))
        return activated
    
    def calculate_conditional_probability(self, condition_atoms, target_atom):
        """
        Calculate conditional probability: P(target_atom | condition_atoms)
        Allow negative probabilities for inhibitory relationships
        """
        # Build condition key
        condition_key = tuple(sorted(condition_atoms))
        
        if condition_key in self.probability_library:
            if target_atom in self.probability_library[condition_key]:
                return self.probability_library[condition_key][target_atom]
        
        # Return default value if no direct conditional probability
        return 0.1
    
    def perceive_environment(self, perception_atoms):
        """
        Environmental Perception Phase: Receive sensory input and activate related logical atoms
        """
        self.activated_atoms.clear()
        self.central_workspace.clear()
        
        # Inject perception atoms into central workspace
        for atom in perception_atoms:
            self.central_workspace.append(atom)
            self.activated_atoms.add(atom)
            
            # Execute Pointing operation to activate related atoms
            related_atoms = self.pointing_operation(atom)
            self.activated_atoms.update(related_atoms)
            self.central_workspace.extend(related_atoms)
    
    def generate_actions(self):
        """
        Generate possible actions based on current situation
        """
        possible_actions = []
        
        # Basic actions
        base_actions = ['flee', 'eat', 'carry']
        
        for action in base_actions:
            if action == 'carry':
                # Carry requires objects
                if 'canned_food' in self.activated_atoms:
                    possible_actions.append(('carry', 'canned_food'))
                if 'scientific_notes' in self.activated_atoms:
                    possible_actions.append(('carry', 'scientific_notes'))
            elif action == 'eat':
                if 'canned_food' in self.activated_atoms:
                    possible_actions.append(('eat', 'canned_food'))
            else:
                possible_actions.append((action, None))
        
        return possible_actions
    
    def calculate_action_weight(self, action, obj, context_atoms):
        """
        Calculate weight for a single action - supporting negative weights and correlations
        """
        total_weight = 0
        context_list = list(context_atoms)
        
        print(f"\n  === Evaluating Action: {action}{' ' + obj if obj else ''} ===")
        
        if action == 'flee':
            # Positive effect of fleeing: reduce death and pain risks
            if 'high_temperature' in context_atoms and 'proximity' in context_atoms and 'body' in context_atoms:
                # Original risk probabilities
                burn_prob = 0.4  # P(burning|high_temperature,proximity,body)
                death_given_burn = 0.1  # P(death|burning,body)
                pain_given_burn = 0.3   # P(pain|burning,body)
                
                original_death_prob = burn_prob * death_given_burn  # 0.04
                original_pain_prob = burn_prob * pain_given_burn    # 0.12
                
                # Risk probabilities after fleeing - flee inhibits proximity (negative correlation)
                run_effectiveness = -0.8  # Negative value indicates inhibition
                reduced_burn_prob = burn_prob * (1 + run_effectiveness)  # 0.4 * 0.2 = 0.08
                reduced_death_prob = reduced_burn_prob * death_given_burn  # 0.008
                reduced_pain_prob = reduced_burn_prob * pain_given_burn    # 0.024
                
                # Weight from death risk reduction
                death_reduction = (original_death_prob - reduced_death_prob) * self.weight_library['death']
                print(f"    Death Risk Reduction: {original_death_prob:.3f} → {reduced_death_prob:.3f}, Weight: {death_reduction:.2f}")
                
                # Weight from pain risk reduction
                pain_reduction = (original_pain_prob - reduced_pain_prob) * self.weight_library['pain']
                print(f"    Pain Risk Reduction: {original_pain_prob:.3f} → {reduced_pain_prob:.3f}, Weight: {pain_reduction:.2f}")
                
                total_weight += death_reduction + pain_reduction
            
        elif action == 'carry' and obj == 'scientific_notes':
            # Trade-off of carrying scientific notes
            positive_weight = 0
            negative_weight = 0
            
            # Positive: civilization continuation
            if 'scientific_notes' in context_atoms:
                civ_prob = self.calculate_conditional_probability(['scientific_notes'], 'civilization_continuation')  # 0.6
                positive_weight = self.weight_library['civilization_continuation'] * civ_prob
                print(f"    Civilization Benefit: {self.weight_library['civilization_continuation']} × {civ_prob} = {positive_weight:.2f}")
            
            # Negative: increased death risk
            if 'high_temperature' in context_atoms and 'proximity' in context_atoms and 'body' in context_atoms:
                # Carrying increases burning probability - positive correlation
                carry_risk_increase = 0.4  # P(burning|carry)
                burn_prob = 0.4 + carry_risk_increase  # Total burning probability 0.8
                death_prob = burn_prob * 0.1  # Death probability 0.08
                
                negative_weight = death_prob * self.weight_library['death']
                print(f"    Death Risk Increase: Burning {0.4}→{burn_prob}, Death {0.04}→{death_prob:.3f}, Weight: {negative_weight:.2f}")
            
            total_weight = positive_weight + negative_weight
            
        elif action == 'carry' and obj == 'canned_food':
            # Trade-off of carrying canned food
            positive_weight = 0
            negative_weight = 0
            
            # Positive: hunger relief (eating inhibits hunger - negative correlation)
            if 'canned_food' in context_atoms:
                hunger_relief_prob = self.calculate_conditional_probability(['canned_food'], 'hunger')  # -0.8
                positive_weight = self.weight_library['hunger'] * hunger_relief_prob  # -5 × -0.8 = 4.0
                print(f"    Hunger Relief: {self.weight_library['hunger']} × {hunger_relief_prob} = {positive_weight:.2f}")
            
            # Negative: increased death risk
            if 'high_temperature' in context_atoms and 'proximity' in context_atoms and 'body' in context_atoms:
                carry_risk_increase = 0.4
                burn_prob = 0.4 + carry_risk_increase
                death_prob = burn_prob * 0.1
                
                negative_weight = death_prob * self.weight_library['death']
                print(f"    Death Risk Increase: Burning {0.4}→{burn_prob}, Death {0.04}→{death_prob:.3f}, Weight: {negative_weight:.2f}")
            
            total_weight = positive_weight + negative_weight
            
        elif action == 'eat' and obj == 'canned_food':
            # Trade-off of eating
            positive_weight = 0
            negative_weight = 0
            
            # Positive: hunger relief (eating inhibits hunger - negative correlation)
            if 'canned_food' in context_atoms:
                hunger_relief_prob = self.calculate_conditional_probability(['eat', 'canned_food'], 'hunger')  # -0.9
                positive_weight = self.weight_library['hunger'] * hunger_relief_prob  # -5 × -0.9 = 4.5
                print(f"    Hunger Relief: {self.weight_library['hunger']} × {hunger_relief_prob} = {positive_weight:.2f}")
                
                # Negative: increased risk while eating in fire
                if 'high_temperature' in context_atoms and 'proximity' in context_atoms:
                    risk_penalty = 0.1  # Slight risk increase
                    negative_weight = risk_penalty * self.weight_library['death']  # 0.1 × -40 = -4.0
                    print(f"    Eating Risk Penalty: {negative_weight:.2f}")
                    
                total_weight = positive_weight + negative_weight
        
        print(f"    Total Weight: {total_weight:.2f}")
        return total_weight
    
    def make_decision(self, perception_atoms):
        """
        Complete cognitive-decision workflow - supporting negative weights
        """
        print("=== Weight-Calculative AI Fire Scenario Decision ===")
        print(f"Perception Input: {perception_atoms}")
        
        # Phase 1: Perception and environmental activation
        self.perceive_environment(perception_atoms)
        print(f"Activated Atoms: {sorted(list(self.activated_atoms))}")
        
        # Display key probability calculations
        print("\n--- Key Risk Probability Calculations ---")
        if 'high_temperature' in self.activated_atoms and 'proximity' in self.activated_atoms and 'body' in self.activated_atoms:
            burn_prob = 0.4
            death_prob = burn_prob * 0.1
            pain_prob = burn_prob * 0.3
            print(f"Base Risk Probabilities:")
            print(f"  P(burning|high_temperature,proximity,body) = {burn_prob}")
            print(f"  P(death|burning,body) = 0.1")
            print(f"  P(pain|burning,body) = 0.3")
            print(f"  ∴ P(death|current_situation) = {burn_prob} × 0.1 = {death_prob:.3f}")
            print(f"  ∴ P(pain|current_situation) = {burn_prob} × 0.3 = {pain_prob:.3f}")
        
        # Phase 2: Action generation
        possible_actions = self.generate_actions()
        print(f"\n--- Generated Feasible Actions ---")
        for i, action in enumerate(possible_actions, 1):
            print(f"  {i}. {action[0]}{' ' + action[1] if action[1] else ''}")
        
        # Phase 3: Action evaluation
        print(f"\n--- Action Weight Evaluation ---")
        action_weights = {}
        for action in possible_actions:
            weight = self.calculate_action_weight(action[0], action[1], self.activated_atoms)
            action_weights[action] = weight
        
        # Phase 4: Decision
        if action_weights:
            best_action = max(action_weights.items(), key=lambda x: x[1])
            print(f"\n=== Final Decision ===")
            print(f"Selected Action: {best_action[0][0]}{' ' + best_action[0][1] if best_action[0][1] else ''}")
            print(f"Decision Weight: {best_action[1]:.2f}")
            
            # Explain decision rationale
            self.explain_decision(best_action[0], best_action[1], action_weights)
            
            return best_action[0], best_action[1]
        else:
            print("No feasible actions available")
            return None, 0
    
    def explain_decision(self, chosen_action, chosen_weight, all_weights):
        """
        Explain decision rationale
        """
        print(f"\n--- Decision Explanation ---")
        action_desc = f"{chosen_action[0]}{' ' + chosen_action[1] if chosen_action[1] else ''}"
        
        print(f"Reason for selecting '{action_desc}':")
        
        if chosen_action[0] == 'flee':
            print("  - In the current fire situation, fleeing maximizes reduction of death and pain risks")
            print("  - Death probability reduced from 4% to 0.8%, pain probability from 12% to 2.4%")
            
        elif chosen_action[0] == 'carry':
            if chosen_action[1] == 'scientific_notes':
                print("  - Carrying scientific notes increases risk but civilization continuation value is high")
                print("  - Prioritize protecting knowledge crucial to human civilization when risk is manageable")
            else:
                print("  - Carrying canned food addresses hunger but risk-reward ratio is low")
                
        elif chosen_action[0] == 'eat':
            print("  - Eating immediately addresses hunger needs")
            print("  - Short-term survival needs prioritized at current risk level")
        
        print(f"\nAlternative Option Weights:")
        for action, weight in sorted(all_weights.items(), key=lambda x: x[1], reverse=True):
            desc = f"{action[0]}{' ' + action[1] if action[1] else ''}"
            print(f"  - {desc}: {weight:.2f}")

# Complete library definitions - supporting negative weights
relation_library = {
    'smoke': ['fire'],
    'fire': ['high_temperature'],
    'high_temperature': ['burning'],
    'proximity': ['burning'],
    'burning': ['pain', 'death'],
    'canned_food': ['eat'],
    'eat': ['hunger'],  # Eating inhibits hunger (negative correlation)
    'flee': ['proximity'],  # Fleeing inhibits proximity (negative correlation)
    'scientific_notes': ['knowledge'],
    'knowledge': ['civilization_continuation'],
    'carry': ['burning']  # Carrying may cause burning (positive correlation)
}

weight_library = {
    'hunger': -5,      # Negative state
    'pain': -10,       # Negative state  
    'death': -40,      # Negative state
    'civilization_continuation': 40   # Positive value
}

probability_library = {
    ('high_temperature', 'proximity', 'body'): {'burning': 0.4},
    ('burning', 'body'): {'death': 0.1, 'pain': 0.3},
    ('canned_food',): {'hunger': -0.8},      # Negative correlation (inhibition)
    ('scientific_notes',): {'civilization_continuation': 0.6},  # Positive correlation
    ('carry',): {'burning': 0.4},            # Positive correlation
    ('flee',): {'proximity': -0.8},          # Negative correlation (inhibition)
    ('eat', 'canned_food'): {'hunger': -0.9} # Negative correlation (inhibition)
}

# Fire scenario test
if __name__ == "__main__":
    # Create AI instance
    ai_system = WeightCalculativeAI(relation_library, weight_library, probability_library)
    
    print("Fire Decision Scenario Simulation")
    print("Situation: Room on fire, canned food and scientific notes available, body in danger")
    print("=" * 60)
    
    perception = ['smoke', 'high_temperature', 'proximity', 'canned_food', 'scientific_notes', 'body']
    decision, weight = ai_system.make_decision(perception)