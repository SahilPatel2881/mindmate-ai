from flask import Flask, render_template, request, jsonify
import random
import datetime
import re
import json
from collections import defaultdict
import statistics

app = Flask(__name__)

print("🧠 ULTIMATE MINDMATE AI - Professional Mental Health Platform Starting...")

class UltimateMindMateAI:
    def __init__(self):
        self.user_profiles = {}
        
        # 🚨 Enhanced Crisis Detection System
        self.CRISIS_KEYWORDS = [
            'suicide', 'kill myself', 'end it all', 'want to die', 'not want to live',
            'end my life', 'better off dead', 'can\'t go on', 'give up', 'harm myself',
            'hurt myself', 'no reason to live', 'everyone would be better without me',
            'going to end it', 'tired of living', 'life is pointless'
        ]
        
        self.CRISIS_RESPONSE = """
🚨 **I'm deeply concerned about your safety**

**IMMEDIATE PROFESSIONAL HELP:**
• **Suicide Prevention Hotline**: 988 (US) or your local emergency number
• **Crisis Text Line**: Text HOME to 741741
• **International Emergency**: 112 or your local emergency services
• **The Trevor Project** (LGBTQ+): 1-866-488-7386

💙 **You are not alone. Professional help is available right now. Your life matters profoundly.**

*Please reach out to these resources immediately. I'm here to support you until you connect with them.*
"""

        # 🎯 Daily Check-in System
        self.daily_checkin_questions = {
            'morning': [
                "🌅 How did you sleep last night? (1-10 scale)",
                "⚡ What's your energy level this morning? (1-10)",
                "🎯 What's one positive intention for today?",
                "💭 Any notable dreams or morning thoughts?"
            ],
            'evening': [
                "📊 How was your overall day? (1-10 scale)",
                "🌪️ What challenged you today?",
                "✨ What went well or made you smile?",
                "🙏 What are you grateful for today?"
            ]
        }

        # 🎯 Wellness Goals System
        self.wellness_goal_templates = {
            'stress_management': {
                'title': "Stress Management Mastery Program",
                'steps': [
                    "Identify your top 3 stress triggers",
                    "Practice 5-minute breathing daily",
                    "Build a 10-minute relaxation routine",
                    "Implement one boundary-setting technique weekly"
                ],
                'timeline': "4 weeks",
                'benefits': "Reduced anxiety, better sleep, improved focus"
            },
            'mood_regulation': {
                'title': "Emotional Balance Journey", 
                'steps': [
                    "Daily mood tracking with insights",
                    "Learn 3 emotion regulation techniques",
                    "Practice cognitive reframing weekly",
                    "Build resilience through small challenges"
                ],
                'timeline': "6 weeks",
                'benefits': "Stable moods, increased self-awareness, emotional resilience"
            },
            'sleep_improvement': {
                'title': "Sleep Restoration Program",
                'steps': [
                    "Consistent bedtime within 30-minute window",
                    "Screen-free hour before sleep",
                    "Evening relaxation practice",
                    "Sleep environment optimization"
                ],
                'timeline': "3 weeks",
                'benefits': "Better energy, improved mood, enhanced cognitive function"
            }
        }

        # 📚 Comprehensive Resource Library
        self.resource_library = {
            'books': {
                'anxiety': {
                    'title': "The Anxiety and Phobia Workbook",
                    'author': "Edmund Bourne",
                    'benefit': "Step-by-step CBT techniques for anxiety management",
                    'level': "Beginner to Advanced"
                },
                'mindfulness': {
                    'title': "Wherever You Go, There You Are",
                    'author': "Jon Kabat-Zinn", 
                    'benefit': "Foundation in mindfulness practice and philosophy",
                    'level': "All Levels"
                },
                'stoicism': {
                    'title': "The Daily Stoic",
                    'author': "Ryan Holiday",
                    'benefit': "Daily wisdom for resilience and perspective",
                    'level': "All Levels"
                },
                'trauma': {
                    'title': "The Body Keeps the Score",
                    'author': "Bessel van der Kolk",
                    'benefit': "Understanding trauma and healing pathways",
                    'level': "Advanced"
                }
            },
            'techniques': {
                'breathing': {
                    'box_breathing': "4-4-4-4 pattern: Inhale 4, hold 4, exhale 4, hold 4 (military technique for calm)",
                    '478_breathing': "Inhale 4, hold 7, exhale 8 - scientifically proven for relaxation",
                    'resonance_breathing': "6 breaths per minute for optimal heart-brain coherence"
                },
                'grounding': {
                    '54321': "5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste (panic attack first aid)",
                    'body_scan': "Progressive attention from toes to head (mindfulness foundation)",
                    'mindful_walking': "Walking with full sensory awareness (moving meditation)"
                },
                'cognitive': {
                    'thought_records': "Document situation → thought → emotion → alternative perspective (CBT core)",
                    'values_clarification': "Identify core values and align actions (ACT approach)",
                    'radical_acceptance': "Accept reality without judgment to reduce suffering (DBT skill)"
                }
            },
            'apps': {
                'meditation': "Insight Timer (free guided meditations, 100,000+ options)",
                'mood_tracking': "Daylio (simple mood and habit tracking with insights)", 
                'breathing': "Breathe (Apple Watch) or Paced Breathing (Android)",
                'cbt': "Woebot (AI CBT companion for daily practice)"
            }
        }

        # 🧠 Neuroscience & Psychology Knowledge Base
        self.neuroscience_knowledge = {
            'brain_regions': {
                'amygdala': "Fear center - becomes overactive in anxiety, can be calmed through breathing",
                'prefrontal_cortex': "Executive function - regulates emotions, strengthened by mindfulness",
                'hippocampus': "Memory center - sensitive to stress, protected by exercise and sleep",
                'anterior_cingulate': "Emotional regulation - involved in both physical and emotional pain"
            },
            'neurotransmitters': {
                'serotonin': "Mood stability - supported by sunlight, exercise, tryptophan-rich foods",
                'dopamine': "Motivation and pleasure - boosted by achievement, social connection, novelty",
                'gaba': "Calming - enhanced by meditation, chamomile, quality sleep",
                'endorphins': "Pain relief and euphoria - released through exercise, laughter, dark chocolate"
            },
            'nervous_system': {
                'sympathetic': "Fight-flight-freeze - activated by stress, calmed by deep breathing",
                'parasympathetic': "Rest-digest-heal - activated by relaxation, meditation, safety",
                'vagus_nerve': "Mind-body connection - stimulated by humming, cold exposure, social connection"
            }
        }

        # 🌟 Achievement & Milestone System
        self.achievements = {
            'conversation_streak': {
                5: "🔥 **5-Day Conversation Streak** - Consistency builds neural pathways for resilience!",
                10: "🌟 **10-Day Engagement Champion** - You're building powerful mental health habits!",
                20: "🎉 **20-Day MindMaster** - Your commitment to growth is inspiring!"
            },
            'goals': {
                'first_goal': "🎯 **Wellness Pioneer** - First goal set! Action precedes motivation.",
                'goal_completed': "✅ **Achievement Unlocked** - Goal completed! Progress creates momentum."
            },
            'techniques': {
                'breathing_regular': "🌬️ **Breathing Pro** - Regular practice regulates your nervous system!",
                'mindfulness_consistent': "🧘 **Mindfulness Regular** - Present-moment awareness growing!"
            }
        }

        # 🎨 Adaptive Communication Styles
        self.communication_styles = {
            'compassionate': {
                'validation': "I hear the depth of what you're sharing...",
                'support': "I'm here with you in this experience...",
                'closing': "Thank you for trusting me with this..."
            },
            'practical': {
                'validation': "That's a common challenge with practical solutions...",
                'support': "Here are actionable steps we can take...",
                'closing': "Let's implement one small change..."
            },
            'inspirational': {
                'validation': "I see strength in how you're facing this...",
                'support': "Remember the resilience you've already shown...",
                'closing': "Your growth journey inspires me..."
            }
        }

    def get_user_context(self, user_id):
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {
                'name': None,
                'mood_history': [],
                'symptom_history': [],
                'conversation_count': 0,
                'last_checkin': None,
                'wellness_goals': [],
                'achievements': [],
                'progress_metrics': {
                    'mood_trends': [],
                    'techniques_used': [],
                    'goals_completed': 0,
                    'checkins_completed': 0,
                    'crisis_events': 0,
                    'engagement_score': 0,
                    'wellness_score': 50
                },
                'personal_preferences': {
                    'wisdom_tradition': None,
                    'learning_style': None,
                    'communication_style': 'adaptive',
                    'checkin_frequency': 'daily'
                },
                'resource_recommendations': [],
                'pattern_insights': [],
                'conversation_context': []
            }
        return self.user_profiles[user_id]

    def detect_crisis_situation(self, text):
        """Advanced crisis detection with context awareness"""
        text_lower = text.lower()
        
        # Immediate crisis keywords
        if any(keyword in text_lower for keyword in self.CRISIS_KEYWORDS):
            return True
        
        # Contextual crisis detection
        crisis_phrases = [
            r"can'?t (?:take|handle|deal) (?:it|this|anymore)",
            r"no (?:point|reason) (?:to live|going on)",
            r"(?:everyone|people) would be better (?:off|without me)",
            r"want (?:to|it) (?:all|everything) to (?:stop|end)",
            r"life is not worth living",
            r"nobody would (?:care|miss) me",
            r"nothing (?:works|helps|matters)"
        ]
        
        for phrase in crisis_phrases:
            if re.search(phrase, text_lower):
                return True
                
        return False

    def should_trigger_daily_checkin(self, user_context):
        """Smart check-in timing"""
        if not user_context['last_checkin']:
            return True
            
        last_checkin = user_context['last_checkin']
        now = datetime.datetime.now()
        hours_since_checkin = (now - last_checkin).total_seconds() / 3600
        
        return hours_since_checkin > 20 or last_checkin.date() != now.date()

    def generate_daily_checkin(self, user_context):
        """Personalized daily check-in"""
        current_hour = datetime.datetime.now().hour
        checkin_type = 'morning' if current_hour < 14 else 'evening'
        
        questions = self.daily_checkin_questions[checkin_type]
        user_context['last_checkin'] = datetime.datetime.now()
        user_context['progress_metrics']['checkins_completed'] += 1
        
        checkin_msg = f"📊 **Daily {checkin_type.capitalize()} Check-in** 🌟\n\nHello {user_context['name']}! Let's check in:\n\n"
        
        for i, question in enumerate(questions, 1):
            checkin_msg += f"{i}. {question}\n"
        
        checkin_msg += f"\nThere are no right or wrong answers - just your honest experience."
        
        return checkin_msg

    def setup_wellness_plan(self, user_context, goal_type):
        """Create personalized wellness plan"""
        if goal_type in self.wellness_goal_templates:
            template = self.wellness_goal_templates[goal_type]
            goal = {
                'id': len(user_context['wellness_goals']) + 1,
                'type': goal_type,
                'title': template['title'],
                'steps': template['steps'],
                'timeline': template['timeline'],
                'benefits': template['benefits'],
                'start_date': datetime.datetime.now().strftime("%Y-%m-%d"),
                'progress': 0,
                'completed_steps': [],
                'active': True
            }
            user_context['wellness_goals'].append(goal)
            
            # Award achievement
            self.award_achievement(user_context, 'first_goal')
            
            return f"""🎯 **New Wellness Goal Created!**

**{goal['title']}**
📅 Timeline: {goal['timeline']}
✨ Benefits: {goal['benefits']}

📝 **Your Steps**:
{chr(10).join(['• ' + step for step in goal['steps']])}

💡 I'll check in on your progress and we can adjust as needed!"""
        else:
            return "I'd love to help you set a wellness goal! Options: stress management, mood regulation, or sleep improvement."

    def recommend_personalized_resources(self, symptoms, user_context):
        """Smart resource recommendations"""
        recommendations = []
        
        if 'anxiety' in symptoms:
            book = self.resource_library['books']['anxiety']
            recommendations.append(f"📚 **Book**: '{book['title']}' by {book['author']}")
            recommendations.append(f"   💡 {book['benefit']} ({book['level']})")
            
            technique = random.choice(list(self.resource_library['techniques']['breathing'].items()))
            recommendations.append(f"🌬️ **Technique**: {technique[0].replace('_', ' ').title()}")
            recommendations.append(f"   📖 {technique[1]}")
            
            recommendations.append(f"📱 **App**: {self.resource_library['apps']['meditation']}")
        
        if 'depression' in symptoms:
            book = self.resource_library['books']['mindfulness']
            recommendations.append(f"📚 **Book**: '{book['title']}' by {book['author']}")
            recommendations.append(f"   💡 {book['benefit']}")
            
            recommendations.append(f"📱 **App**: {self.resource_library['apps']['mood_tracking']}")

        if recommendations:
            user_context['resource_recommendations'].extend(recommendations)
            header = "💡 **Personalized Resources for You:**\n\n"
            return header + "\n".join(recommendations[:4])  # Limit to 4 items
        return None

    def detect_behavioral_patterns(self, user_context):
        """Advanced pattern detection"""
        if len(user_context['mood_history']) < 7:
            return []
        
        patterns = []
        moods_by_weekday = defaultdict(list)
        
        for entry in user_context['mood_history'][-21:]:  # Last 3 weeks
            if 'weekday' in entry:
                moods_by_weekday[entry['weekday']].append(entry['mood'])
        
        # Analyze patterns
        for weekday, moods in moods_by_weekday.items():
            if len(moods) >= 3:
                negative_ratio = moods.count('negative') / len(moods)
                if negative_ratio > 0.6:
                    patterns.append(f"Challenges often appear on {weekday}s")
                elif negative_ratio < 0.2:
                    patterns.append(f"{weekday}s tend to be positive days")
        
        return patterns[:2]  # Return top 2 patterns

    def generate_comprehensive_progress_report(self, user_context):
        """Generate detailed progress report"""
        if user_context['conversation_count'] < 3:
            return None
        
        report = "📈 **Your Personal Progress Report**\n\n"
        
        # Basic metrics
        report += f"• **Total Conversations**: {user_context['conversation_count']}\n"
        report += f"• **Check-ins Completed**: {user_context['progress_metrics']['checkins_completed']}\n"
        report += f"• **Active Wellness Goals**: {len([g for g in user_context['wellness_goals'] if g['active']])}\n"
        report += f"• **Wellness Score**: {user_context['progress_metrics']['wellness_score']}/100\n"
        
        # Mood analysis
        if len(user_context['mood_history']) >= 5:
            recent_moods = [entry['mood'] for entry in user_context['mood_history'][-7:]]
            if recent_moods:
                positive_pct = (recent_moods.count('positive') / len(recent_moods)) * 100
                report += f"• **Recent Positive Mood**: {positive_pct:.0f}%\n"
        
        # Pattern insights
        patterns = self.detect_behavioral_patterns(user_context)
        if patterns:
            report += f"\n🔍 **Pattern Insights**:\n"
            for pattern in patterns:
                report += f"• {pattern}\n"
        
        # Achievements
        if user_context['achievements']:
            report += f"\n🏆 **Recent Achievements**:\n"
            for achievement in user_context['achievements'][-2:]:
                report += f"• {achievement}\n"
        
        report += f"\n🌟 **Keep shining, {user_context['name']}!** Every step forward matters."
        
        return report

    def award_achievement(self, user_context, achievement_type):
        """Award achievements for milestones"""
        if achievement_type == 'first_goal' and len(user_context['wellness_goals']) == 1:
            achievement = self.achievements['goals']['first_goal']
        elif achievement_type == 'conversation_streak':
            count = user_context['conversation_count']
            if count in self.achievements['conversation_streak']:
                achievement = self.achievements['conversation_streak'][count]
            else:
                return None
        else:
            return None
        
        if achievement not in user_context['achievements']:
            user_context['achievements'].append(achievement)
            return achievement
        return None

    def calculate_wellness_score(self, user_context):
        """Calculate comprehensive wellness score"""
        base_score = 50  # Starting point
        
        # Engagement bonus
        base_score += min(20, user_context['conversation_count'] * 2)
        
        # Consistency bonus
        if user_context['progress_metrics']['checkins_completed'] > 3:
            base_score += 15
        
        # Goal progress bonus
        active_goals = [g for g in user_context['wellness_goals'] if g['active']]
        if active_goals:
            base_score += 10
        
        # Technique usage bonus
        technique_entries = [m for m in user_context['mood_history'] if m.get('has_technique')]
        if len(technique_entries) > 2:
            base_score += 5
        
        return min(100, base_score)

    def generate_quick_support_response(self, intensity_level):
        """Immediate support for urgent needs"""
        quick_support = {
            'high': "🚨 **Immediate Support**: Breathe with me. 4-7-8 pattern. You're safe. This will pass.",
            'medium': "🌬️ **Quick Calm**: Box breathing. 4-4-4-4. You've got this.",
            'low': "💫 **Grounding**: Notice your feet on floor. 3 deep breaths. Present moment."
        }
        return quick_support.get(intensity_level, "I'm here with you. What do you need?")

    def extract_name(self, text):
        """Advanced name extraction"""
        patterns = [
            r'(?:my name is|i am|call me|name is|this is) (\w+)',
            r'^(\w+)$',
            r'^(?:i\'m|im) (\w+)',
            r'(?:you can call me|please call me) (\w+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                name = match.group(1).capitalize()
                if len(name) > 2 and name not in ['Sad', 'Happy', 'Good', 'Bad', 'Fine', 'Okay', 'Hello', 'Hi']:
                    return name
        return None

    def analyze_symptoms(self, text):
        """Comprehensive symptom analysis"""
        symptoms = {
            'chest_pain': ['chest', 'heart', 'pain in chest', 'chest hurts', 'tight chest', 'chest pressure', 'heart pain'],
            'headache': ['headache', 'head pain', 'migraine', 'head hurts', 'head pounding'],
            'stomach_issues': ['stomach', 'nausea', 'belly', 'abdomen', 'gut', 'stomach pain'],
            'anxiety': ['anxious', 'nervous', 'worried', 'panic', 'overwhelmed', 'scared', 'fearful'],
            'depression': ['depressed', 'sad', 'hopeless', 'empty', 'nothing matters', 'worthless'],
            'anger': ['angry', 'mad', 'furious', 'rage', 'frustrated', 'irritated'],
            'fatigue': ['tired', 'exhausted', 'fatigued', 'no energy', 'burned out', 'drained']
        }
        
        detected = []
        text_lower = text.lower()
        
        for symptom, keywords in symptoms.items():
            if any(keyword in text_lower for keyword in keywords):
                detected.append(symptom)
                
        return detected

    def analyze_sentiment(self, text):
        """Enhanced sentiment analysis"""
        positive_words = ['happy', 'good', 'great', 'awesome', 'well', 'better', 'excited', 'joy', 'peaceful', 'calm', 'grateful', 'content', 'hopeful']
        negative_words = ['sad', 'bad', 'terrible', 'awful', 'anxious', 'stressed', 'depressed', 'angry', 'tired', 'exhausted', 'hopeless', 'pain', 'hurt', 'worst']
        
        score = 0
        text_lower = text.lower()
        
        for word in positive_words:
            score += text_lower.count(word)
        for word in negative_words:
            score -= text_lower.count(word)
                
        if score > 0:
            return 'positive'
        elif score < 0:
            return 'negative'
        else:
            return 'neutral'

    def generate_ultimate_response(self, user_input, user_context):
        """Main response generator with all features"""
        
        # 🚨 CRISIS DETECTION - FIRST PRIORITY
        if self.detect_crisis_situation(user_input):
            user_context['progress_metrics']['crisis_events'] += 1
            return self.CRISIS_RESPONSE
        
        input_lower = user_input.lower()
        user_context['conversation_count'] += 1
        
        print(f"🎯 Conversation: {user_context['conversation_count']}, User: {user_context.get('name', 'Unknown')}")

        # FIRST CONVERSATION: Enhanced welcome
        if user_context['conversation_count'] == 1:
            return self.get_ultimate_welcome_message()

        # Process name if not set
        if not user_context['name']:
            extracted_name = self.extract_name(user_input)
            if extracted_name:
                user_context['name'] = extracted_name
                return self.get_personalized_welcome(user_context)
            else:
                user_context['name'] = "Friend"
                return self.get_personalized_welcome(user_context)

        # 🚨 URGENT SUPPORT for intense emotions
        if any(word in input_lower for word in ['panic', 'overwhelmed', 'cant cope', 'emergency', 'help now']):
            quick_response = self.generate_quick_support_response('high')
            return quick_response

        # 📊 DAILY CHECK-IN SYSTEM
        if self.should_trigger_daily_checkin(user_context) and user_context['conversation_count'] > 2:
            return self.generate_daily_checkin(user_context)

        # 🎯 WELLNESS GOAL SYSTEM
        if any(word in input_lower for word in ['goal', 'plan', 'program', 'want to improve', 'work on']):
            goal_types = ['stress_management', 'mood_regulation', 'sleep_improvement']
            for goal_type in goal_types:
                if goal_type.replace('_', ' ') in input_lower:
                    return self.setup_wellness_plan(user_context, goal_type)
            return "I'd love to help you set wellness goals! Are you looking to manage stress, regulate mood, or improve sleep?"

        # 📈 PROGRESS REPORT REQUESTS
        if any(word in input_lower for word in ['progress', 'report', 'how am i doing', 'my improvement', 'tracking']):
            report = self.generate_comprehensive_progress_report(user_context)
            if report:
                return report
            else:
                return "Let's have a few more conversations first, then I'll be able to provide meaningful progress insights!"

        # Analyze symptoms and context
        detected_symptoms = self.analyze_symptoms(user_input)
        user_context['symptom_history'].extend(detected_symptoms)
        
        # Update all tracking systems
        self.update_comprehensive_metrics(user_context, detected_symptoms, user_input)
        
        # Generate main therapeutic response
        response = self.generate_therapeutic_response(user_input, detected_symptoms, user_context)
        
        # 📚 ADD RESOURCE RECOMMENDATIONS (30% chance)
        if random.random() < 0.3:
            resources = self.recommend_personalized_resources(detected_symptoms, user_context)
            if resources:
                response += f"\n\n{resources}"
        
        # 🏆 CHECK AND AWARD ACHIEVEMENTS
        streak_achievement = self.award_achievement(user_context, 'conversation_streak')
        if streak_achievement:
            response += f"\n\n{streak_achievement}"
        
        # 📊 PROGRESS INSIGHTS (every 5 conversations)
        if user_context['conversation_count'] % 5 == 0:
            patterns = self.detect_behavioral_patterns(user_context)
            if patterns:
                response += f"\n\n🔍 **Pattern Insight**: {patterns[0]}"
        
        return response

    def get_ultimate_welcome_message(self):
        return """🌠 **Welcome to ULTIMATE MindMate AI** 

I'm your complete mental wellness partner, featuring:

🧠 **Neuroscience-Based Support** - Understand your brain's responses
🎯 **Personalized Wellness Goals** - Structured programs for growth  
📊 **Progress Tracking** - Insights and pattern detection
📚 **Resource Library** - Books, techniques, and apps
🚨 **Crisis Support** - Immediate professional resources
🎨 **Adaptive Communication** - Tailored to your needs

💫 **My commitment**: Your sustainable mental wellbeing journey

What should I call you?"""

    def get_personalized_welcome(self, user_context):
        name = user_context['name']
        return f"""Wonderful to meet you, {name}! 🌈

I'm here to be your comprehensive mental wellness companion. 

🚀 **Ready to explore**:
• Daily check-ins to track your journey
• Personalized wellness goals  
• Neuroscience-backed techniques
• Progress insights and patterns
• Curated resources and tools

💬 **What would you like to start with today?**
- "I'd like to set a wellness goal"
- "I'm feeling [emotion/physical sensation]"  
- "Tell me about daily check-ins"
- Or just share what's on your mind"""

    def update_comprehensive_metrics(self, user_context, symptoms, user_input):
        """Update all tracking systems"""
        mood = self.analyze_sentiment(user_input)
        
        user_context['mood_history'].append({
            'timestamp': datetime.datetime.now(),
            'mood': mood,
            'symptoms': symptoms,
            'input_length': len(user_input),
            'weekday': datetime.datetime.now().strftime('%A'),
            'has_technique': any(word in user_input.lower() for word in ['breathe', 'meditate', 'technique', 'exercise'])
        })
        
        # Update wellness score
        user_context['progress_metrics']['wellness_score'] = self.calculate_wellness_score(user_context)

    def generate_therapeutic_response(self, user_input, symptoms, user_context):
        """Generate therapeutic response with all knowledge bases"""
        response_parts = []
        user_name = user_context['name']
        
        # Handle physical symptoms with neuroscience
        if 'chest_pain' in symptoms:
            response_parts.append(f"""I understand you're experiencing chest discomfort, {user_name}.

🧠 **Neuroscience Insight**: 
Your amygdala (fear center) is signaling threat, activating sympathetic nervous system. This causes chest muscle tension and breathing changes.

🫁 **Nervous System Regulation**:
• **Box Breathing**: 4-4-4-4 pattern to calm the system
• **Cold Compress**: On chest or neck to stimulate vagus nerve
• **Progressive Relaxation**: Release chest and shoulder tension

💡 **Consider**: This could be your body's way of expressing emotional stress.""")
        
        # Handle emotional states
        emotional_responses = []
        if 'anxiety' in symptoms:
            emotional_responses.append(f"""I hear the anxiety, {user_name}.

🌊 **Polyvagal Theory Approach**:
We need to restore your social engagement system (ventral vagal state).

🚨 **Immediate Tools**:
• **54321 Grounding**: Engage all senses - 5 things you see, 4 touch, 3 hear, 2 smell, 1 taste
• **Resonance Breathing**: 6 breaths/minute for heart-brain coherence
• **Bilateral Stimulation**: Alternate tapping left-right sides

🔬 **Brain Science**: Your prefrontal cortex can regulate amygdala responses with practice.""")
        
        if 'depression' in symptoms:
            emotional_responses.append(f"""I hear the heaviness, {user_name}.

⚡ **Behavioral Activation**:
Action before motivation - start tiny and build momentum.

🌅 **Neuroplasticity Opportunity**:
New activities create new neural pathways. Even small actions count.

🎯 **Evidence-Based Approach**:
• Morning sunlight for circadian regulation
• Micro-social connections for reward system activation
• Values-based action for meaning restoration""")
        
        if emotional_responses:
            response_parts.append("\n\n".join(emotional_responses))
        
        # General adaptive support
        if not response_parts:
            response_parts.append(self.generate_adaptive_support(user_input, user_name, user_context))
        
        return "\n\n".join(response_parts)

    def generate_adaptive_support(self, user_input, user_name, user_context):
        """Adapt support based on user history"""
        
        if user_context['conversation_count'] > 5:
            wellness_score = user_context['progress_metrics']['wellness_score']
            if wellness_score > 70:
                return f"You're doing amazing work with your wellbeing, {user_name}! What would you like to explore today?"
            elif wellness_score > 40:
                return f"Thanks for your consistent engagement, {user_name}. How can I support you today?"
            else:
                return f"I'm here to support you, {user_name}. What's present for you right now?"
        else:
            approaches = [
                f"What's on your heart and mind today, {user_name}?",
                f"How can I be most helpful to you in this moment, {user_name}?",
                f"What would you like to focus on in our conversation, {user_name}?"
            ]
            return random.choice(approaches)

# Initialize the ultimate AI system
ultimate_ai = UltimateMindMateAI()

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'response': 'No data received'}), 400
            
        user_message = data.get('message', '')
        user_id = data.get('user_id', 'default_user')
        
        print(f"📨 Received: {user_message}")
        
        if not user_message:
            return jsonify({'response': 'Please share what\'s on your mind...'})
        
        # Get user context and generate response
        user_context = ultimate_ai.get_user_context(user_id)
        ai_response = ultimate_ai.generate_ultimate_response(user_message, user_context)
        
        print(f"🤖 Response generated for {user_context.get('name', 'Unknown')}")
        
        return jsonify({
            'response': ai_response,
            'user_name': user_context.get('name', 'Friend')
        })
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'response': 'I encountered an error while processing. Please try again.'}), 500

@app.route('/progress/<user_id>')
def get_progress(user_id):
    """Comprehensive progress endpoint"""
    if user_id in ultimate_ai.user_profiles:
        user_context = ultimate_ai.user_profiles[user_id]
        
        progress_data = {
            'user_name': user_context.get('name', 'Friend'),
            'conversation_count': user_context['conversation_count'],
            'wellness_score': user_context['progress_metrics']['wellness_score'],
            'engagement_score': user_context['progress_metrics']['engagement_score'],
            'checkins_completed': user_context['progress_metrics']['checkins_completed'],
            'active_goals': len([g for g in user_context['wellness_goals'] if g['active']]),
            'achievements_count': len(user_context['achievements']),
            'recent_achievements': user_context['achievements'][-3:],
            'pattern_insights': ultimate_ai.detect_behavioral_patterns(user_context)
        }
        
        return jsonify(progress_data)
    return jsonify({'error': 'User not found'})

@app.route('/goals/<user_id>')
def get_goals(user_id):
    """Get user's wellness goals"""
    if user_id in ultimate_ai.user_profiles:
        return jsonify(ultimate_ai.user_profiles[user_id]['wellness_goals'])
    return jsonify({'error': 'User not found'})

@app.route('/resources/<symptom_type>')
def get_resources(symptom_type):
    """Get resources for specific symptoms"""
    resources = ultimate_ai.recommend_personalized_resources([symptom_type], {'name': 'User'})
    if resources:
        return jsonify({'resources': resources})
    return jsonify({'error': 'No resources found for that symptom type'})

if __name__ == '__main__':
    print("🌟 MindMate AI Server Ready!")
    print("📍 Access at: http://127.0.0.1:5000")
    print("🚀 Features: Crisis Support, Progress Tracking, Wellness Goals, Neuroscience Insights")
    app.run(debug=True, port=5000, host='0.0.0.0')