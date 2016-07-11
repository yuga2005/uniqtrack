function sg_reflow_page() {
   if ( document.body.clientWidth < 600 )
       document.body.className = 'narrow';
   else
       document.body.className = '';
};

function sg_setup_on_load() {
    sg_reflow_page();
    document.getElementById('user_login').focus();
    document.body.addEventListener( 'resize', sg_reflow_page );
};

window.addEventListener( 'load', sg_setup_on_load );
