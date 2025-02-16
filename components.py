def create_project_card(project):
    return f"""
    <div class='project-card'>
        <div class='support-badge'>SUPPORTED</div>
        <div class='favorite-icon'>⭐</div>
        <br>
        <h5 class='project-title'>{project['title']}</h5>
        <div class='metadata-item'>
            <span class='metadata-label'>Task:</span>
            <span class='metadata-value'>{project['task']}</span>
        </div>
        <div class='metadata-item'>
            <span class='metadata-label'>Model:</span>
            <span class='metadata-value'>{project['model']}</span>
        </div>
        <p class='project-description'>{project['description']}</p>
        <br>
        <a class="demo-button" color=white href="http://localhost:8501/{project['href']}"> Go to DEMO </a>
    
    </div>
    """

def create_project_section(projects):
    cards = "".join([create_project_card(project) for project in projects])
    return f"""
    <div class='title'><h3>PROJECTS DEMO</h3></div>
    <br>
    <div class='card-container'>
        {cards}
    </div>
    """
