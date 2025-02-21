css = """
.title {text-align: center;}
.card-container {
    display: flex;
    justify-content: flex-start;  
    gap: 24px;
    flex-wrap: wrap;
    margin: 2rem auto;
    padding: 0 1rem;
    max-width: 1000px;
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
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.support-badge {
    position: absolute;
    top: -12px;
    left: 24px;
    background-color: #7c3aed;
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
    color: #3b82f6;
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
    background-color: #98AFC7;  /* Greyish blue color */
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
}

.demo-button:hover {
    background-color: #47525b;  /* Darker greyish blue on hover */
    box-shadow: 0 2px 4px rgba(90, 103, 114, 0.2);
    transform: translateY(-1px);
}

.demo-button {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0.4rem 1rem;
    background-color: #98AFC7;
    color: white !important;
    border: none;
    border-radius: 0.375rem;
    font-size: 0.875rem;
    font-weight: 500;
    text-align: center;
    text-decoration: none !important;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 1px 2px rgba(90, 103, 114, 0.1);
    width: 100%;
}

.demo-button:hover {
    background-color: #7A92B4 !important;
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