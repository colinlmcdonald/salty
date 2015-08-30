# Surfers

"Surfers" is a "web application" (very loosely; there's no actual
interactivity, just viewing of data -- the R part of a CRUD application) for viewing
information about surfboard shapers, the surfboards they shape, and the surfers
that ride them.  Yes, this is essentially the canonical "Authors and Books" Django
example, with a little salty ocean flavor for fun.

## Getting Started

0. Clone the repository.

      $ git clone git@bitbucket.org:fareharbor/surfers salty
      $ cd salty

0. Create a virtual environment.

      $ mkdir ~/python-environments
      $ virtualenv ~/python-environments/salty
      $ source ~/python-environments/salty/bin/activate

0. Install dependencies.

      $ pip install -r requirements.txt

0. Create and populate your database.

      $ ./new-db

0. Run the development server.

      $ ./manage.py runserver_plus

0. Visit <http://localhost:8000> in your browser.

## Code Overview

As in many (most?) Django applications, the core of Surfers is really the (very simple)
data model. We have three models: `Surfer` represents individual surfers that might own
0 (just getting started!), 1, or many surfboards. `Shaper` for shapers that might have made
0+ surfboards (gotta start somewhere!) and `Surfboard` for the actual surfboards themselves.
The data associated with each of these models is kinda irrelevant -- we're really more
worried about the relationships between them, and anyway I wasn't really sure
what users might actually care about, so I kinda tossed it together haphazardly.

After that we really only have views  (the routing layer is trivial), which
basically just render our templates with a bit of data.  Not a whole lot going on.

# Projects

We've identified a couple of projects you might take on, involving updating this
project to add features, fix bugs, or whatnot.

An important consideration in each of these projects is that the implementation
be "production quality" -- we're not looking for skunkworks approaches that validate
the business need (though we do that "in real life" all the time).  Instead we're
looking for an approach that takes care to demonstrate what you consider "best
practices", from various perspectives. For instance, in terms of code quality
and structure, some questions we might ask: Is it DRY, or are there glaring
redundancies? Or have you gone overboard on abstraction? Are things named well?
Is it "Pythonic", whatever that means?) Performance is also a concern: Does
it use 80 bajillion GB of RAM? Does it do 700 queries? Is it O(N^3) when O(N)
would do? And of course, at the end of the day, is it correct?

It's therefore better to take a smaller or simpler approach, and nail it, than
to toss in everything and the kitchen sink in a less-than-quality way.

Also, you should feel free to change anything and everything about the data
model, views, routes, and so on -- just remember that this is "already in
production", so have a migration strategy in mind, even if you don't implement
it.

## Collaboration Station

Turns out that shapers sometimes collaborate on a new shape, but our data model
only allows for one shaper per surfboard. Shit! Let's see about updating our
data model so that surfboards can be shaped by *one or more* shapers. We will also
want to update our views so that anywhere we are currently display the shaper
associated with a surfboard, we instead show all shapers associated with it.

## This One's a Good One

Sometimes you're just a surfer looking for a new stick. Come up with a way to 
determine a recommendation or set of recommendations for a surfer, and add it
to the surfer view (`/surfers/<pk>/`).  Ideally we're looking for a "good"
way to recommend a new surfboard for a surfer, so be ready to argue that your
method is at least halfway decent (`random` I'm looking at you).

## It's Not All One-Offs

Not every new surfboard is a completely unique snowflake; instead shapers often
will make a few "models" in various dimensions.  Let's say we want to update our
data model to support this usecase.  An approach would be to add a `SurfboardModel`
model, whereby shapers that previously would have several surfboards, would now
have several models, each with 1 or more surfboards associated with it.  Any
surfboards that were one-offs would nevertheless get their own surfboard model.

A surfboard model would have a `name` and a `description` at least.  After that
the important concern is again not the fields but the *relationships*. Once you've
got the data model sorted, update the views to focus attention on surfboard models.
Finally, make sure you've got a view for an individual model that shows all associated
surfboards.
