css = """
.title {text-align: center;}
.card-container {
    display: flex;
    justify-content: flex-start;  
    gap: 24px;
    flex-wrap: wrap;
    margin: 2rem auto;
    padding: 0 1rem;
    max-width: 1150px;
}
.project-card {
    background-color: white;
    padding: 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    width: calc(33.333% - 24px);
    max-width: 355px;
    min-width: 305px;
    position: relative;
    transition: all 0.3s ease;
    margin-bottom: 24px;
    flex: 1 1 calc(33.333% - 24px);
}
.project-card:hover {
    box-shadow: 0 6px 8px rgba(0,80,142,0.35)
}
.support-badge {
    position: absolute;
    top: -12px;
    left: 24px;
    background-color: #6691be;
    color: white;
    padding: 4px 16px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 0.875rem;
    z-index: 1;
}
.favorite-icon {
    position: absolute;
    top: 16px;
    right: 16px;
    color: #fb923c;
}
.project-title {
    color: #3b82f6;
    font-size: 0.9rem;
    font-weight: 500;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.metadata-item {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
}
.metadata-label {
    color: #4b5563;
    font-weight: 500;
    min-width: 60px;
}
.metadata-value {
    color: #769bc2;
    flex: 1;
}
.project-description {
    color: #4b5563;
    margin-top: 1rem;
    line-height: 1.2;
}

/* Responsive breakpoints */
@media (max-width: 1024px) { 
    .project-card {
        width: calc(50% - 12px);
        flex: 1 1 calc(50% - 12px);
    }
}
@media (max-width: 768px) { 
    .project-card {
        width: 100%;
        flex: 1 1 100%;
    }
}

.demo-button {
    display: flex;
    justify-content: center;  /* Centers the button */
    align-items: center;  /* Vertically centers the content */
    padding: 0.4rem 1rem;  /* Narrower height */
    background-color: #9db7d2;  /* Greyish blue color */
    color: white;
    border: none;
    border-radius: 0.375rem;
    font-size: 0.875rem;
    font-weight: 500;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 1px 2px rgba(90, 103, 114, 0.1);
    width: 100%;  /* Ensures button spans the full width */
    margin-top: auto; /* Pushes button to bottom */
}

.demo-button:hover {
    background-color: #47525b;  /* Darker greyish blue on hover */
    box-shadow: 0 2px 4px rgba(90, 103, 114, 0.2);
    transform: translateY(-1px);
}

.demo-button:link, .demo-button:visited {
    color: white !important;
    text-decoration: none !important;
}


.centered-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Full height */
}
    

"""

experience_css = """
    <style>
    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: #2c3e50;
        text-align: center;
        position: relative;
        padding-bottom: 15px;
    }
    .section-title:after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 70px;
        height: 3px;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
    }
    .experience-container {
        max-width: 850px;
        margin: 0 auto;
    }
    .experience-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 25px;
        overflow: hidden;
        transition: all 0.3s ease;
        border: 1px solid #eaeaea;
    }
    .experience-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border-color: #dadada;
    }
    .card-header {
        padding: 20px 25px;
        border-bottom: 1px solid #f0f0f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .company-info {
        flex-grow: 1;
    }
    .company-name {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 5px;
    }
    .job-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #3498db;
        margin-bottom: 8px;
    }
    .job-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        font-size: 0.9rem;
        color: #7f8c8d;
    }
    .meta-item {
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .meta-icon {
        color: #3498db;
    }
    .logo-placeholder {
        width: 60px;
        height: 60px;
        background-color: #f8f9fa;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #7f8c8d;
        font-weight: 600;
        font-size: 1.2rem;
    }
    .card-body {
        padding: 20px 25px;
    }
    .job-description {
        color: #34495e;
        line-height: 1.6;
    }
    .highlight-tag {
        display: inline-block;
        background-color: #e3f2fd;
        color: #1976d2;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-right: 8px;
        margin-top: 8px;
    }
    .timeline-container {
        margin-top: 40px;
        position: relative;
        padding: 25px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #eaeaea;
    }
    .timeline-title {
        font-size: 1.6rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 20px;
        text-align: center;
    }
    .company-logo {
    width: 90px;
    height: 90px;
    display: flex;
    align-items: center;
    justify-content: center;
    }
    .company-logo img {
        max-width: 100%;
        max-height: 100%;
        border-radius: 8px;
        object-fit: contain;
    }
    </style>
    """


education_css = """
    <style>
    .education-section-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: #2c3e50;
        text-align: center;
        position: relative;
        padding-bottom: 15px;
    }
    .education-section-title:after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 70px;
        height: 3px;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
    }
    .education-container {
        max-width: 850px;
        margin: 0 auto;
    }
    .education-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 25px;
        overflow: hidden;
        transition: all 0.3s ease;
        border: 1px solid #eaeaea;
        display: flex;
    }
    .education-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border-color: #dadada;
    }
    .education-logo {
        width: 90px;
        background-color: #f8f9fa;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 15px;
        border-right: 1px solid #f0f0f0;
    }
    .logo-placeholder {
        width: 90px;
        height: 90px;
        background-color: #f0f0f0;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #7f8c8d;
        font-weight: 600;
        font-size: 1.5rem;
    }
    .education-details {
        padding: 20px 25px;
        flex-grow: 1;
    }
    .university-name {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 8px;
    }
    .degree {
        font-size: 1.15rem;
        font-weight: 600;
        color: #3498db;
        margin-bottom: 10px;
    }
    .duration {
        font-size: 0.95rem;
        color: #7f8c8d;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    </style>
    """

experience_card_template = """
<div class="experience-card">
    <div class="card-header">
        <div class="company-info">
            <div class="job-title">{role}</div>
            <div class="company-name">{company}{department}</div>
            <div class="job-meta">
                <div class="meta-item">
                    <span class="meta-icon">🗓️</span>
                    <span>{duration} · {tenure}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-icon">📍</span>
                    <span>{location}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-icon">💼</span>
                    <span>{type}</span>
                </div>
            </div>
        </div>
        {logo_html}
    </div>
    <div class="card-body">
        <div class="job-description">{description}</div>
        <div style="margin-top: 15px;">
            {highlights_html}
        </div>
    </div>
</div>
"""