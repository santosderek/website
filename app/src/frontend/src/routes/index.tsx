import { component$ } from "@builder.io/qwik";
import type { DocumentHead } from "@builder.io/qwik-city";


import  { Navigation } from "../components/navigation/nav.tsx";

export default component$(() => {
  return (
    <>
    <Navigation />
      <h1>Hi 👋</h1>
      <div>
        Can't wait to see what you build with qwik! Hello!
        <br />
        Happy coding.
      </div>
    </>
  );
});

export const head: DocumentHead = {
  title: "Welcome to Qwik",
  meta: [
    {
      name: "description",
      content: "Qwik site description",
    },
  ],
};
