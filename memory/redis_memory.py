import redis

redis_client = redis.Redis(host='localhost', port=6379)

def save_session(session_id, data):
    redis_client.set(session_id, str(data))

def get_session(session_id):
    return redis_client.get(session_id)
