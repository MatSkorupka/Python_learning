import random
from datetime import datetime, timedelta

def log_analyzer():
    """
    Create a generator that simulates processing server logs:
    
    Each log entry should contain:
    - timestamp
    - user_id (random number 1-100)
    - action ('login', 'logout', 'purchase', 'view')
    - status ('success', 'error')
    - processing_time (random 1-1000 ms)

    Requirements:
    1. Generate random log entries
    2. Calculate average processing time
    3. Flag suspicious activity (more than 5 actions per user)
    4. Track number of errors
    """
    # Your code here
    
    current_time = datetime.now()
    user_actions = {}  # Track actions per user
    total_processing_time = 0
    total_entries = 0
    error_count = 0

    while True:
        try:
            # Generate log entry
            user_id = random.randint(1, 100)
            action = random.choice(['login', 'logout', 'purchase', 'view'])
            status = random.choice(['success', 'error'])
            processing_time = random.randint(1, 1000)

            # Track user actions
            user_actions[user_id] = user_actions.get(user_id, 0) + 1
            
            # Track statistics
            total_processing_time += processing_time
            total_entries += 1
            if status == 'error':
                error_count += 1

            # Create log entry
            log_entry = {
                'timestamp': current_time,
                'user_id': user_id,
                'action': action,
                'status': status,
                'processing_time': processing_time,
                'avg_processing_time': total_processing_time / total_entries,
                'suspicious': user_actions[user_id] > 5,
                'error_rate': error_count / total_entries
            }

            current_time += timedelta(seconds=random.randint(1, 60))
            yield log_entry

        except Exception as e:
            yield {
                'timestamp': current_time,
                'status': 'error',
                'error_message': str(e)
            }

# Test
log_gen = log_analyzer()
for _ in range(5):
    print(next(log_gen))