# whats-up-doc
Bug Tracker built with Django


    requires logging in, but people who aren't logged in cannot create accounts (don't want any random person to see bugs in your application!)
    use a custom user model to replace the built-in one (you may want to reference 👨‍🔬 Under the Microscope: Custom Users)
    has a homepage that shows all tickets, arranged in separate columns according to current ticket status (i.e. New, In Progress, Done, Invalid)
    allows filing/creating tickets
    has a ticket detail page
    allows assigning a ticket to the currently logged in user
    allows marking a ticket as invalid
    allows marking a ticket as complete
    allows editing tickets (we will limit this to Title and Description, do not include other any of the other fields)
    has a user detail page where you can see:
        the current tickets assigned to a user
        which tickets that user has filed
        which tickets that user completed

# References: 

Worked with Chris Wilson and Sean Bailey, also received some input from Peter Marsh made comments throughout assessment where assistance was required! Also have links attached to certain comments where stackoverflow was helpful! Also followed along with Instructor Joe's Demos :)
