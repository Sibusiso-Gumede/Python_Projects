The purpose of the project is to get data about the top rated python projects
from the GitHub API and make a visual representation of it. The 'requests'
http library is used to make an API call and store the response by specifying
the Uniform Resource Locator and the headers for the API application version.
We access the 'status_code' data member of the response object to check if the
request was successful. 

Initially the data is in JavaScript Object Notation when the response is captured.
So, we then make use of the 'json()' method found in the 'requests' library to
translate the data to a dictionary. We then proceed to process the project repositories
elements into lists that will cater to our graph visualization needs.

We use nested dictionaries to generate the attributes of the plotly library interactive graph.
The graph is then stored as a HTTP file that can be viewed offline using a browser.

Compile the program and run it. The HTTP file will be stored on the working directory during
compile-time.