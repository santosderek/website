import { component$ } from "@builder.io/qwik";
import type { DocumentHead } from "@builder.io/qwik-city";


import  { Navigation } from "../components/navigation/nav.tsx";
import { Terminal } from "../components/terminal/terminal.tsx";

export default component$(() => {
  return (
    <>
        <Navigation />
        <Terminal />
    </>
  );
});

export const head: DocumentHead = {
  title: "Derek Santos",
  meta: [
    {
      name: "description",
      content: "Derek's Personal Site",
    },
  ],
};
