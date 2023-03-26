


$(document).ready(function(){
    if($('.comment').text().length > 48){

        $('.comment').css('display' , 'block')
    }

    $('#comar').on( 'keydown' ,function(event){
        if(event.keyCode === 13){
            var myrep = `
            <div class="single_comment">
                
                <img src="clientpic" class="client_pic">
                        
                <div class="comment_and_name">
                    <p class="client_name"><span> clientname</span></p>
                    <p class="comm" ><span> clientcomment </span></p>
                </div>
            </div>
        `;
            var text=$('#comar').val()
            var csrf=$('input[name=csrfmiddlewaretoken]').val()
            var slugy=$('#describe').val()
        
            $.ajax({
                url : '/add_comment/',
                type : 'POST',
                data : {
                    dec_slugy : slugy,
                    text_data : text,
                    csrfmiddlewaretoken : csrf
                },
                success : function(response){
                    let myrep1 =  myrep.replace('clientname' , response.clientname)
                    .replace('clientcomment' , response.comment)
                    .replace('clientpic' ,  response.clientpic)
                        if(response.active){

                        if(response.comment!=''){
                            $('.comment').css('display' , 'block')
                            $('.comment').append(myrep1)  
                            $('#comar').val('')
                            
                            
                        }
                    } else {
                        
                    }
                    
                }
            })
        
        }
    })

});