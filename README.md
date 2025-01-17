# University Attendance Monitoring Application


This project was developed to modernize the attendance tracking system for university professors, addressing a request from the **Islamic Azad University of Zanjan**. The traditional method of managing attendance and absences was outdated and inefficient, prompting the creation of this system to provide a more streamlined and user-friendly solution.

## Key Features

- **Role-Based Access Control**: Tailored access based on user roles and authority levels, ensuring that users only see the information relevant to their position.
- **Comprehensive Reporting**: Generate detailed reports on professors’ attendance and activities, enabling university officials to make informed decisions. Reports can be provided to key stakeholders, such as:
  - Department managers
  - Faculty heads
  - Education department leaders
  - Accounting department heads
  - General education departments
  - University presidents

## Future Enhancements

In the next phase of the project, we plan to expand the system's capabilities to include:
- **Student Attendance Tracking**: Enable monitoring and management of university students' attendance and absences.
- **SMS Notifications**: Notify students and professors about attendance status and updates directly through SMS integration.

This system is designed to improve operational efficiency, provide transparency, and reduce the administrative burden of managing attendance in academic institutions.



## Technologies and Libraries Used  

- **Django and DRF:** Manage the backend and APIs for a robust and scalable system.  
- **Docker:** Simplifies deployment by containerizing the application and its dependencies.  
- **Nginx:** Acts as a reverse proxy and serves static files, enhancing application performance and security.
- **Gunicorn:** Efficiently serves the application in production.  
- **JWT:** Ensures secure user authentication and authorization.  
- **Linux Cron Jobs:** Automates tasks, including holiday-specific system behavior.  
- **Data Libraries:** Tools like `openpyxl`, `pandas`, and `numpy` handle data import, processing, and validation for each university semester.  
- **jdatetime:** Converts Gregorian dates to Solar Hijri for regional compatibility.   


The project maintains separate environments for development and production:  
- **SQLite** is used during development for ease of setup.  
- **PostgreSQL** powers the production environment for reliability and scalability.  


## How to run

```bash
$ docker compose -f docker-compose.prod.yml up -d --build
```

## Environment variables
This project uses environment variables to manage sensitive and configurable settings.
Before deploying, ensure that **all necessary environment variables are updated** to match your production environment. 
Improper configuration may lead to security vulnerabilities or operational issues.    

1. **`.env.prod`**  
   - This file contains general production environment settings.  

2. **`.env.prod.db`**  
   - This file is used for configuring the PostgreSQL database connection.  

### Admin Panel Access  

The application includes an admin panel that can be accessed at:  
- **URL:** `http://localhost/admin` or `http://127.0.0.1/admin`  

Default superuser credentials are as follows:  
- **Username:** `admin`  
- **Password:** `123456`  

You can use these credentials for initial access. To enhance security, it is highly recommended to update the superuser username and password in the `# Superuser settings` section of the `.env.prod` file.  



## License
The MIT License (MIT)


