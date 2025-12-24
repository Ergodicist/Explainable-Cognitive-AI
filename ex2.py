# Chapter 5: Alien Ecosystem Risk Assessment Scenario
# Demonstrating Analogical Reasoning and Dynamic Learning in Novel Situations

class AlienEcosystemAI:
    def __init__(self, relation_library, weight_library, probability_library, earth_knowledge_base):
        """
        Initialize Alien Ecosystem AI based on Weight-Calculative architecture
        """
        self.relation_library = relation_library
        self.weight_library = weight_library
        self.probability_library = probability_library
        self.earth_knowledge_base = earth_knowledge_base  # Earth biology knowledge
        self.activated_atoms = set()
        self.central_workspace = []
        self.learned_relations = {}  # Dynamically learned relationships
        self.similarity_scores = {}
        
    def pointing_operation(self, source_atom):
        """
        Pointing Operation: Activate related logical atoms
        """
        activated = set()
        # Check both static and learned relations
        all_relations = {**self.relation_library, **self.learned_relations}
        
        if source_atom in all_relations:
            for target_atom in all_relations[source_atom]:
                activated.add(target_atom)
                # Recursively activate related atoms
                activated.update(self.pointing_operation(target_atom))
        return activated
    
    def comparison_operation(self, alien_feature, earth_concept):
        """
        Comparison Operation: Calculate similarity between alien features and earth concepts
        Returns similarity score between 0 and 1
        """
        # Multi-dimensional similarity calculation
        structural_similarity = self.calculate_structural_similarity(alien_feature, earth_concept)
        functional_similarity = self.calculate_functional_similarity(alien_feature, earth_concept)
        behavioral_similarity = self.calculate_behavioral_similarity(alien_feature, earth_concept)
        
        # Weighted average of similarity dimensions
        total_similarity = (structural_similarity * 0.4 + 
                          functional_similarity * 0.4 + 
                          behavioral_similarity * 0.2)
        
        self.similarity_scores[(alien_feature, earth_concept)] = total_similarity
        return total_similarity
    
    def calculate_structural_similarity(self, alien, earth):
        """
        Calculate structural similarity based on physical properties
        """
        structural_properties = {
            'purple_glow': ['bioluminescence', 'pigmentation', 'light_emission'],
            'crystal_movement': ['crystal_structure', 'mineral_composition', 'solid_state'],
            'transparent_phase_shift': ['phase_transition', 'transparency', 'state_change']
        }
        
        if alien in structural_properties:
            alien_props = set(structural_properties[alien])
            earth_props = set(self.get_earth_concept_properties(earth))
            common = alien_props.intersection(earth_props)
            return len(common) / max(len(alien_props), 1)
        return 0.1
    
    def calculate_functional_similarity(self, alien, earth):
        """
        Calculate functional similarity based on purpose/role
        """
        functional_roles = {
            'purple_glow': ['energy_metabolism', 'communication', 'defense'],
            'crystal_movement': ['locomotion', 'growth', 'information_transfer'],
            'transparent_phase_shift': ['energy_absorption', 'camouflage', 'reproduction']
        }
        
        if alien in functional_roles:
            alien_roles = set(functional_roles[alien])
            earth_roles = set(self.get_earth_functional_roles(earth))
            common = alien_roles.intersection(earth_roles)
            return len(common) / max(len(alien_roles), 1)
        return 0.1
    
    def calculate_behavioral_similarity(self, alien, earth):
        """
        Calculate behavioral similarity based on patterns
        """
        behavioral_patterns = {
            'purple_glow': ['rhythmic', 'responsive', 'collective'],
            'crystal_movement': ['directed', 'purposeful', 'adaptive'],
            'transparent_phase_shift': ['reversible', 'stimulus_response', 'cyclic']
        }
        
        if alien in behavioral_patterns:
            alien_patterns = set(behavioral_patterns[alien])
            earth_patterns = set(self.get_earth_behavioral_patterns(earth))
            common = alien_patterns.intersection(earth_patterns)
            return len(common) / max(len(alien_patterns), 1)
        return 0.1
    
    def get_earth_concept_properties(self, concept):
        """Get properties of earth biological concepts"""
        earth_properties = {
            'bioluminescence': ['light_emission', 'chemical_reaction', 'energy_release'],
            'pheromone': ['chemical_signal', 'communication', 'molecular'],
            'crystal_growth': ['crystal_structure', 'mineral_composition', 'slow_movement'],
            'amoeba_movement': ['cytoplasmic_streaming', 'pseudopodia', 'slow_motion']
        }
        return earth_properties.get(concept, [])
    
    def get_earth_functional_roles(self, concept):
        """Get functional roles of earth concepts"""
        earth_roles = {
            'bioluminescence': ['communication', 'predation', 'defense'],
            'pheromone': ['communication', 'mating', 'territory'],
            'crystal_growth': ['growth', 'mineralization', 'structure_building'],
            'amoeba_movement': ['locomotion', 'feeding', 'exploration']
        }
        return earth_roles.get(concept, [])
    
    def get_earth_behavioral_patterns(self, concept):
        """Get behavioral patterns of earth concepts"""
        earth_patterns = {
            'bioluminescence': ['rhythmic', 'stimulus_response', 'species_specific'],
            'pheromone': ['diffusion_based', 'concentration_dependent', 'species_specific'],
            'crystal_growth': ['slow', 'directional', 'environment_dependent'],
            'amoeba_movement': ['exploratory', 'food_seeking', 'adaptive']
        }
        return earth_patterns.get(concept, [])
    
    def assess_novelty(self, alien_features):
        """
        Assess overall novelty of alien ecosystem compared to earth biology
        """
        print("=== Novelty Assessment ===")
        total_similarity = 0
        comparisons = 0
        
        earth_concepts = ['bioluminescence', 'pheromone', 'crystal_growth', 'amoeba_movement']
        
        for alien_feature in alien_features:
            for earth_concept in earth_concepts:
                similarity = self.comparison_operation(alien_feature, earth_concept)
                total_similarity += similarity
                comparisons += 1
                print(f"  {alien_feature} vs {earth_concept}: {similarity:.3f}")
        
        overall_similarity = total_similarity / comparisons if comparisons > 0 else 0
        novelty_score = 1 - overall_similarity
        
        print(f"Overall Similarity to Earth Biology: {overall_similarity:.3f}")
        print(f"Novelty Score: {novelty_score:.3f}")
        
        return novelty_score, overall_similarity
    
    def dynamic_learning(self, alien_features, earth_concepts):
        """
        Dynamically learn new relationships based on comparisons
        """
        print("\n=== Dynamic Knowledge Expansion ===")
        
        for alien_feature in alien_features:
            # Find most similar earth concept
            best_match = None
            best_similarity = 0
            
            for earth_concept in earth_concepts:
                similarity = self.similarity_scores.get((alien_feature, earth_concept), 0)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = earth_concept
            
            if best_match and best_similarity > 0.2:  # Learning threshold
                # Learn new relationships based on partial similarity
                self.learn_relationships(alien_feature, best_match, best_similarity)
    
    def learn_relationships(self, alien_feature, earth_concept, similarity):
        """
        Learn new pointing relationships for alien features
        """
        print(f"Learning relationships for {alien_feature} based on {earth_concept} (similarity: {similarity:.3f})")
        
        if alien_feature == 'purple_glow' and earth_concept == 'bioluminescence':
            self.learned_relations['purple_glow'] = ['energy_metabolism', 'communication_system']
            print("  → Learned: purple_glow → energy_metabolism")
            print("  → Learned: purple_glow → communication_system")
            
        elif alien_feature == 'crystal_movement' and earth_concept == 'crystal_growth':
            self.learned_relations['crystal_movement'] = ['information_transfer', 'structural_adaptation']
            print("  → Learned: crystal_movement → information_transfer")
            print("  → Learned: crystal_movement → structural_adaptation")
            
        elif alien_feature == 'transparent_phase_shift' and earth_concept == 'amoeba_movement':
            self.learned_relations['transparent_phase_shift'] = ['energy_absorption', 'environment_interaction']
            print("  → Learned: transparent_phase_shift → energy_absorption")
            print("  → Learned: transparent_phase_shift → environment_interaction")
    
    def generate_actions(self):
        """
        Generate possible actions for alien ecosystem scenario
        """
        return [
            ('immediate_research', None),
            ('cautious_retreat', None), 
            ('remote_monitoring', None)
        ]
    
    def calculate_action_weight(self, action, context_atoms):
  
        total_weight = 0
        novelty_score = self.similarity_scores.get('overall_novelty', 0.5)
        
        print(f"\n  === Evaluating Action: {action[0]} ===")
        
        if action[0] == 'immediate_research':
            # High scientific benefit but also high safety risk
            science_benefit = self.weight_library['scientific_discovery'] * (1 - novelty_score) * 2.0
            safety_risk = self.weight_library['crew_safety'] * novelty_score * 1.5
            
            print(f"    Scientific Benefit: {self.weight_library['scientific_discovery']} × {1-novelty_score:.3f} × 2.0 = {science_benefit:.3f}")
            print(f"    Safety Risk: {self.weight_library['crew_safety']} × {novelty_score:.3f} × 1.5 = {safety_risk:.3f}")
            
            total_weight = science_benefit + safety_risk
            
        elif action[0] == 'cautious_retreat':
            # Maximum safety, but complete loss of scientific opportunity
            safety_benefit = self.weight_library['crew_safety'] * novelty_score * 0.8  # Positive safety impact
            opportunity_cost = self.weight_library['scientific_discovery'] * (1 - novelty_score) * 0.3
            
            print(f"    Safety Benefit: {self.weight_library['crew_safety']} × {novelty_score:.3f} × 0.8 = {safety_benefit:.3f}")
            print(f"    Opportunity Cost: {self.weight_library['scientific_discovery']} × {1-novelty_score:.3f} × 0.3 = {opportunity_cost:.3f}")
            
            total_weight = safety_benefit + opportunity_cost
            
        elif action[0] == 'remote_monitoring':
            # Balanced approach - moderate science with good safety
            science_benefit = self.weight_library['scientific_discovery'] * (1 - novelty_score) * 1.2
            safety_benefit = self.weight_library['crew_safety'] * novelty_score * 0.6  # Positive safety impact
            
            print(f"    Scientific Benefit: {self.weight_library['scientific_discovery']} × {1-novelty_score:.3f} × 1.2 = {science_benefit:.3f}")
            print(f"    Safety Benefit: {self.weight_library['crew_safety']} × {novelty_score:.3f} × 0.6 = {safety_benefit:.3f}")
            
            total_weight = science_benefit + safety_benefit
        
        print(f"    Total Weight: {total_weight:.3f}")
        return total_weight

    def make_decision(self, alien_features):
        """
        Complete decision process for alien ecosystem scenario
        """
        print("=== Weight-Calculative AI: Alien Ecosystem Risk Assessment ===")
        print(f"Alien Features Detected: {alien_features}")
        
        # Phase 1: Novelty assessment through comparison operations
        novelty_score, overall_similarity = self.assess_novelty(alien_features)
        self.similarity_scores['overall_novelty'] = novelty_score
        
        # Phase 2: Dynamic learning based on partial similarities
        earth_concepts = ['bioluminescence', 'pheromone', 'crystal_growth', 'amoeba_movement']
        self.dynamic_learning(alien_features, earth_concepts)
        
        # Phase 3: Action generation and evaluation
        possible_actions = self.generate_actions()
        print(f"\n--- Generated Actions ---")
        for i, action in enumerate(possible_actions, 1):
            print(f"  {i}. {action[0]}")
        
        # Phase 4: Weight calculation for each action
        print(f"\n--- Action Weight Evaluation ---")
        action_weights = {}
        for action in possible_actions:
            weight = self.calculate_action_weight(action, self.activated_atoms)
            action_weights[action] = weight
        
        # Phase 5: Decision with explanation
        if action_weights:
            best_action = max(action_weights.items(), key=lambda x: x[1])
            print(f"\n=== Final Decision ===")
            print(f"Selected Action: {best_action[0][0]}")
            print(f"Decision Confidence: {best_action[1]:.3f}")
            
            self.explain_alien_decision(best_action[0], best_action[1], action_weights, novelty_score)
            
            return best_action[0], best_action[1]
        else:
            print("No valid decision could be made")
            return None, 0
    
    def explain_alien_decision(self, chosen_action, chosen_weight, all_weights, novelty_score):
        """
        Provide detailed explanation for alien ecosystem decision
        """
        print(f"\n--- Decision Explanation ---")
        print(f"Selected '{chosen_action[0]}' because:")
        
        if chosen_action[0] == 'remote_monitoring':
            print("  - Novel biological features detected with significant differences from Earth lifeforms")
            print(f"  - Overall similarity to Earth biology: {1-novelty_score:.3f}")
            print("  - Primary considerations: 'crew_safety' vs 'scientific_discovery'")
            print("  - Balanced approach ensures crew safety while maintaining scientific observation")
            
        elif chosen_action[0] == 'cautious_retreat':
            print("  - Highly novel and potentially dangerous biological systems detected")
            print("  - Safety concerns outweigh potential scientific benefits")
            print("  - Conservative approach prioritizes crew survival")
            
        elif chosen_action[0] == 'immediate_research':
            print("  - Sufficient similarities to Earth biology provide reasonable safety margins")
            print("  - High scientific value justifies calculated risks")
            print("  - Opportunity for groundbreaking discoveries")
        
        print(f"\nAlternative Options:")
        for action, weight in sorted(all_weights.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {action[0]}: {weight:.3f}")

# Alien Ecosystem Knowledge Base
relation_library = {
    'bioluminescence': ['energy_metabolism', 'communication', 'defense_mechanism'],
    'pheromone': ['chemical_communication', 'reproduction', 'social_organization'],
    'crystal_growth': ['mineral_nutrition', 'structural_development', 'slow_motion'],
    'amoeba_movement': ['cytoplasmic_movement', 'food_acquisition', 'environment_exploration'],
    'energy_metabolism': ['life_sustenance', 'growth_potential'],
    'communication_system': ['social_behavior', 'coordination', 'intelligence_potential'],
    'defense_mechanism': ['threat_response', 'survival_capability']
}

weight_library = {
    'crew_safety': -80,           # High negative weight for safety risks
    'scientific_discovery': 60,   # High positive weight for discovery
    'mission_success': 40,        # Moderate positive for mission objectives
    'resource_conservation': 20   # Low positive for efficiency
}

probability_library = {
    ('high_novelty',): {'safety_risk': 0.7, 'scientific_opportunity': 0.9},
    ('medium_novelty',): {'safety_risk': 0.3, 'scientific_opportunity': 0.6},
    ('low_novelty',): {'safety_risk': 0.1, 'scientific_opportunity': 0.3}
}

# Test the alien ecosystem scenario
if __name__ == "__main__":
    # Create AI instance
    alien_ai = AlienEcosystemAI(relation_library, weight_library, probability_library, {})
    
    print("Alien Ecosystem Risk Assessment Scenario")
    print("Situation: Unknown alien lifeforms with unusual characteristics detected")
    print("=" * 70)
    
    alien_features = ['purple_glow', 'crystal_movement', 'transparent_phase_shift']
    decision, confidence = alien_ai.make_decision(alien_features)