from .flack import app
from .utils import timestamp

# We use a list to calculate requests per second
request_stats = []


def add_request():
    t = timestamp()
    while len(request_stats) > 0 and \
            request_stats[0] < t - app.config['REQUEST_STATS_WINDOW']:
        del request_stats[0]
    request_stats.append(t)


def requests_per_second():
    return len(request_stats) / app.config['REQUEST_STATS_WINDOW']