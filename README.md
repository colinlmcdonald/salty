# Surfers

"Surfers" is a "web application" (very loosely; there's no actual
interactivity, just viewing of data -- the R part of a CRUD application) for viewing
information about surfboard shapers, the surfboards they shape, and the surfers
that ride them.  Yes, this is essentially the canonical "Authors and Books" Django
example, with a little salty ocean flavor for fun.

## Existing Code

As in many (most?) Django applications, the core of Surfers is really the (very simple)
data model. We have three models: `Surfer` represents individual surfers that might own
0 (just getting started!), 1, or many surfboards. `Shaper` for shapers that might have made
0+ surfboards (gotta start somewhere!) and `Surfboard` for the actual surfboards themselves.
The data associated with each of these models is kinda irrelevant -- we're really more
worried about the relationships between them, and anyway I wasn't really sure
what users might actually care about, so I kinda tossed it together haphazardly.

After that we really only have views  (the routing layer is trivial), which
basically

# The Project

We've identified a couple of projects you might take on

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

## Collaboration Station

Turns out that shapers sometimes collaborate on a new shape, but our data model
only allows for one shaper per surfboard. Shit! Let's see about updating our
data model so that surfboards can be shaped by *one or more* shapers. We will also
want to update our views so that anywhere we are currently display the shaper
associated
 

## This One's a Good One

Finally

## It's Not All One-Offs

Not every new surfboard is a completely unique snowflake; instead shapers often
will make a few "models" in various dimensions.  Let's say we want to update our
data model to support this usecase.  An approach would be to add a `SurfboardModel`
model, whereby shapers that previously would have several surfboards, would now
have several models, each with 1 or more surfboards associated with it.  Any
surfboards that were one-offs would nevertheless get their own surfboard model.

A surfboard model would have a `name` and a `description` at least.  When displaying

In terms of rendering this information to the user, we'd
