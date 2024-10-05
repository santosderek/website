import { component$ } from "@builder.io/qwik";
import type { DocumentHead } from "@builder.io/qwik-city";

export const Navigation = component$(() => {

    return (
        <nav>
        <a href="/#experience">Experience</a>
        <a href="/#skills">Skills</a>
        <a href="/#projects">Projects</a>
        <a href="/#resume">Resume</a>
        <a href="/#contact">Contact</a>
        <img src="/images/santosderek.png" alt="Derek Santos" style="max-width: 50em;" />
        <a href="https://github.com/santosderek" target="_blank" rel="noopener noreferrer">
            <img src="/images/svg/github.svg" alt="github" style="max-width: 2em;" />
        </a>
        <a href="https://linkedin.com/in/santosderek" target="_blank" rel="noopener noreferrer">
            <img src="/images/svg/linkedin.svg" alt="linkedin" style="max-width: 2em;" />
        </a>
        <a href="mailto:santos.jon.derek@gmail.com">
            <img src="/images/svg/envelope.svg" alt="email" style="max-width: 2em;" />
        </a>
        <a href="/resume">
            <img src="/images/svg/download.svg" alt="resume" style="max-width: 2em;" />
        </a>
        </nav>
    );
    }
);
