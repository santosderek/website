export const projectPages = {
  project: {
    title: 'Projects',
    subtitle: 'A place for project details.',
    sections: [
      {
        title: 'Project Overview',
        paragraphs: ['Select one of the highlighted projects from the home page to see more implementation details.'],
      },
    ],
  },
  santosderek: {
    title: 'SantosDerek.com',
    subtitle: 'My personal website and dynamic resume.',
    sections: [
      {
        title: 'Project Overview',
        paragraphs: [
          'In order to showcase my projects and experience using specific technologies, I have decided to create a resource where users may view an overview of my latest achievements. This website is also a project within itself since all aspects of the website was created using Python, Docker, Github Actions, and Ansible. Below is a dive into the work, and features this website holds under the hood as well as the deployment of the website itself.',
        ],
      },
      {
        title: 'A Dynamic Home Page',
        paragraphs: [
          'The landing page is now a React Router single-page app that loads the same JSON resource data exposed by the Flask API. This keeps the content workflow dynamic while making the frontend easier to expand with richer interactions.',
          'The data is organized and parsed from a series of JSON files found within the resources folder of the repository. When updating the home page of my website, I only need to add or remove entries within these JSON files, and the contents of the page should adjust automatically on the next request.',
        ],
      },
      {
        title: 'Automatic Resume Creator',
        paragraphs: ['Upon runtime of the web application, the JSON resource files are used to create a structured and styled Word Document entirely using the python-docx module. This Word Document is the very same file given when visiting the /resume route.'],
      },
      {
        title: 'Deployment Architecture',
        image: '/static/images/santosderek/santosderekDeployment.png',
        imageAlt: 'Santosderek deployment',
        paragraphs: [
          'The deployment process of the website involves the usage of Github, Github Actions, DigitalOcean, Ansible, and Docker. When committing changes, I push the respective commits to Github where upon creating a pull request will trigger a workflow to verify all unit tests pass. The workflow also verifies and builds the Dockerfile to be deployed. After all checks pass, I accept the pull request and first deploy the updated Docker image to a test environment within my homelab using Ansible. Once my inspection is complete within the test environment, I run a second Ansible script which deploys the code to the Digital Ocean droplet, updating the docker image to the most recent change, and serves the flask application through santosderek.com.',
        ],
      },
    ],
    links: [{ title: 'Github', href: 'https://github.com/santosderek/website', text: 'View the source on github!' }],
  },
  vitality: {
    title: 'Vitality',
    subtitle: 'An all in one platform allowing users to connect to nearby trainers, schedule meetings, share workouts, and encourage healthy dieting.',
    mission: {
      image: '/static/images/vitality/FrontPage.png',
      imageAlt: 'Vitality Front Page',
      text: 'A free and centralized web application that allows users to take charge of their health by connecting with real trainers, recieve personalized workouts, and guidance with dietary plans recommended to you. Users can also find gyms and recreation centers in your area, and ultimately become part of a community that values and promotes healthy living.',
    },
    features: [
      { image: '/static/images/vitality/ShowTrainers.png', text: 'Invite and connect with trainers near you by searching through our diverse set of trainers ready to guide you through workouts. Search is based on username or full names, where a trainee can send an invitation to connect.' },
      { image: '/static/images/vitality/TrainersNearYou.png', text: 'Integration with Google Maps allows trainees the ability to get a sense of the availability around their area. Insipired by Tesla\'s Supercharger Map, trainees can select points within the map to view trainer names around their area.' },
      { image: '/static/images/vitality/CreateEvents.png', text: 'Schedule meetings with trainers detailing specific workouts and meeting times to added trainers.' },
      { image: '/static/images/vitality/Diets.png', text: 'View diets from select categories through Youtube recommendations on diets and workouts.' },
      { image: '/static/images/vitality/Workouts.png', text: 'Create, search, and view workouts from other trainers and earn experience points on the difficulty you could accomplish!' },
    ],
    technologies: ['Python', 'Flask', 'Github Actions', 'Docker', 'Nginx', 'Ansible'],
    sections: [
      {
        title: 'Project Overview',
        paragraphs: [
          'Vitality is a web application devoted to helping trainers and trainees search and connect with one another, while also providing the means to share schedules, dietary recommendations, and workout information in one centralized user interface. There is a diverse range of exercise applications that exist already but none bring together the ability to search for a trainer, schedule a workout, create a workout with a trainer, and share recommendations through the use of youtube videos within one easy to use interface, independent of what platform users decide to surf the web on.',
          'Our focus on flexibility allows us to cover a higher demographic of devices than existing mobile applications or desktop applications. Vitality was developed with a responsive design which dynamically adjusts to all ranges of device resolutions and layouts. No matter how a user chooses to view our application, Vitality will automatically adjust and scale to a user’s needs.',
        ],
      },
      {
        title: 'Deployment Architecture',
        image: '/static/images/vitality/DeploymentDiagram.png',
        imageAlt: 'Deployment Diagram',
        paragraphs: [
          'As soon as the project started within sprint one, our scrum master wanted the deployment to be as automated as soon as possible. This includes unit testing, verification that a code review has been done on each pull request, and deploying the application to a virtual server in the cloud.',
          'To make use of continuous integration practice, our project uses three main technologies, Git, Github, and Ansible. Git serves as our version control software which allows the team to create sub-branches of the mainline code being deployed, and tinker with the code before merging back into the master branch.',
          'Lastly, an Nginx reverse proxy is set up to enable support for HTTPS and redirect all unencrypted traffic to the encrypted channel. The Nginx proxy is independent of the application and is only a means to redirect and encrypt traffic.',
        ],
      },
    ],
    links: [
      { title: 'Live Demo', href: 'https://vitality.santosderek.com', text: 'View the live demo!' },
      { title: 'Github', href: 'https://github.com/santosderek/Vitality', text: 'View source on github!' },
    ],
  },
};
