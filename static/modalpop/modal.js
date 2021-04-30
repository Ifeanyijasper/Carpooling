(($ => {
    $(() => {
      $.prototype.fullscreen = function()
      {
        var $e = $(this);
        if(!$e.hasClass('modal-fullscreen')) return;
        bind($e);
      }
      
      function cssn($e, props) {
        let sum = 0;
        props.forEach(p => {
          sum += parseInt($e.css(p).match(/\d+/)[0]);
        });
        return sum;
      }
      function g($e)
      {
        return {
          width: cssn($e, ['margin-left', 'margin-right', 'padding-left', 'padding-right', 'border-left-width', 'border-right-width']),
          height: cssn($e, ['margin-top', 'margin-bottom', 'padding-top', 'padding-bottom', 'border-top-width', 'border-bottom-width']),
        };
      }
      function calc($e)
      {
        const wh = $(window).height();
        const ww = $(window).width();
        const $d = $e.find('.modal-dialog');
        $d.css('width', 'initial');
        $d.css('height', 'initial');
        $d.css('max-width', 'initial');
        $d.css('margin', '5px');
        const d = g($d);
        const $h = $e.find('.modal-header');
        const $f = $e.find('.modal-footer');
        const $b = $e.find('.modal-body');
        $b.css('overflow-y', 'scroll');
        const bh = wh - $h.outerHeight() - $f.outerHeight() - ($b.outerHeight()-$b.height()) - d.height;
        $b.height(bh);
      }
      function bind($e)
      {
         $e.on('show.bs.modal', e => {
          const $e = $(e.currentTarget).css('visibility', 'hidden');
         });
         $e.on('shown.bs.modal', e => {
          calc($(e.currentTarget));
          const $e = $(e.currentTarget).css('visibility', 'visible');   
         });
      }
      $(window).resize(() => {
        calc($('.modal.modal-fullscreen.in'));
      });
      bind($('.modal-fullscreen'));
    });
  }))(jQuery);

  <h4><a data-toggle="modal" data-target="#myModal" id="trigger-btn">Route: {{ user_request.ride }}</a></h4>
                                    <div class="modal fade modal-fullscreen" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                                        <div class="modal-dialog" role="document">
                                          <div class="modal-content">
                                            <div class="modal-header">
                                              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                              <h4 class="modal-title" id="myModalLabel">Modal title</h4>
                                            </div>
                                            <div class="modal-body">
                                                <h2><a href="#" >{{ user_request.ride.start }} to {{ ride.dest }}</a></h2>
                                                <h4>  <a href="#"><i class="fa fa-cab"></i> Ride : {{ ride.vehicle }}</a></h4>
                                                <span> <i class="fa fa-user"></i> Seating : {{ ride.no_pass }} seats</span>
                                                <span><p> <i class="fa fa-calendar"></i> Start time:
                                                    {{ ride.date }} at <i class="fa fa-clock-o"></i> {{ ride.start_time }}</p>
                                                </span>
                                                <span> <p> <i class="fa fa-calendar"></i> Estimated arrival time:
                                                    {{ ride.date }} at <i class="fa fa-clock-o"></i> {{ ride.arrival_time }}</p>
                                                </span>
            
                                                <span> <p> <i class="fa fa-male"></i><i class="fa fa-female"></i> Gender Preference:
                                                        {{ ride.sex }}</p>
                                                </span>
            
                                                    <span> <p> <i class="fa fa-money"></i> Cost:
                                                        {{ ride.cost }} fcfa/km</p>
                                                </span>
            
                                                <h4>  <a href="#"><i class="glyphicon glyphicon-user"></i> Driver : {{ ride.user.full_name }}</a></h4>               
                                            </div>
                                            <div class="modal-footer">
                                              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                              <button type="button" class="btn btn-primary">Save changes</button>
                                            </div>
                                          </div>
                                        </div>
                                      </div>