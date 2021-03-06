# guitar_tabs
_The objective of this assignment was to create a Django web app that lets you search for guitar tabs from an external source, subverting advertisements, redirects and cookie tracking._

The learning objectives were as follows:
- Build a Django web application that scrapes its data from an external source and display it back to the user as if it belonged to your site.
- Allow an anonymous (non logged in user) to search for a song name
- Display the search results as a clickable link that does NOT take you away from your site. (links that take you to the external site are allowed but are required to be marked as such)
- The link should take you to an internal page on your site and show an advertisement free experience where a user can easily read the guitar tablature.

Based upon the assignment outlines above, I chose to use www.guitartabs.cc for getting the guitar tabs.  The application was written in Python using Django's framework.  I also used Python's requests library and BeautifulSoup.
