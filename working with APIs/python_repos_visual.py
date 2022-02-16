import requests

from plotly.graph_objs import Bar
from plotly import offline

def getData():
    """It makes an API request and returns the requested contents."""
    
    # Make an API call and store the response.
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    # Make use of the latest GitHub API version.
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    # Ensure the request was successful before returning
    # any data.
    if r.status_code != 200:
        raise(requests.RequestException)
    
    return r

def createGraph(the_response):
    """Processes 'the_response' and creates a bar graph displaying the data."""
    
    # Process the results.
    response_dict = the_response.json()
    repo_dicts = response_dict['items']
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        # Create a hyperlink for the user to click and get sent to the GitHub.
        # website.
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])
        
        # Data about each project to generate the tooltip 
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    # Make a visualization.
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    # The graph layout specifications.
    my_layout = {
        'title': 'Most-Starred Python Project on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    # Create the graph and make it available in offline mode.
    offline.plot(fig, filename='python_repos_styled.html')

if __name__ == '__main__':
    response = getData()
    createGraph(response)