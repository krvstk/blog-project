      <li><a href="{% url 'posts:about' %}">About</a></li>
      <li><a href="{% url 'posts:contact' %}">Contact</a></li>

        <a class="navbar-brand" href="{% url 'posts:list' %}">Dolph</a>

            <form class="navbar-form navbar-right">
      <div class="form-group">
        <input type="text" name="q" placeholder="Search posts" value="{{request.GET.q}}"/>
      </div>
      <button type="submit" class="btn btn-primary btn-md"><i class="glyphicon glyphicon-search"></i></button>
    </form>
