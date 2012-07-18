Mobile Visibility
-----------------

`Zurb Foundation <http://foundation.zurb.com/>`_ includes a series of visibility classes that  
allow you to hide or display content on various devices using 'show/hide-for-x' where "x" can be 
a xlarge, large, medium and small. For example if we include the following snippet on the line corresponding to the device 
that you are currently using will be displayed ::

    <strong class="show-for-xlarge">You are on a very large screen.</strong>
    <strong class="show-for-large">You are on a large screen.</strong>
    <strong class="show-for-large-up">You are on a large or very large screen.</strong>
    <strong class="show-for-medium">You are on a medium screen.</strong>
    <strong class="show-for-medium-down">You are on a medium or small screen.</strong>
    <strong class="show-for-small">You are on a small screen, like a smartphone.</strong>


Conversely including ::

   <strong class="hide-for-xlarge">You are not on a very large screen.</strong>
   <strong class="hide-for-large">You are not on a large screen.</strong>
   <strong class="hide-for-large-up">You are not on a large or very large screen.</strong>
   <strong class="hide-for-medium-down">You are not on a medium or small screen.</strong>
   <strong class="hide-for-medium">You are not on a medium screen.</strong>
   <strong class="hide-for-small">You are not on a small screen.</strong>
   
Will display the two lines corresponding to the devices that you are not using.
