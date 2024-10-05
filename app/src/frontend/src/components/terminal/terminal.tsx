import { component$ } from "@builder.io/qwik";
import type { DocumentHead } from "@builder.io/qwik-city";

import styles from "./terminal.module.css";


export const Terminal = component$(() => {

    return (
        <>
            <section class={styles["terminal-section"]}>
                <div class={styles.terminal}>
                    <div class={styles["terminal-header"]}>
                        <nav class={styles["terminal-header-buttons"]}>
                            <span class="control-item control-minimize">‒</span>
                            <span class="control-item control-maximize">□</span>
                            <span class="control-item control-close">˟</span>
                        </nav>
                    </div>
                    <main class={styles["terminal-body"]}>
                        <div class={styles["window-cursor"]}>
                            <span class="i-cursor-indicator">> who -u | pixelify</span>
                        </div>
                        <div class={styles["terminal-flex-container"]}>
                            <div class={styles["terminal-flex-item-1 terminal-body-header"]}>
                                <p>Derek Santos</p>
                            </div>
                            <div class={styles["terminal-flex-item-2 terminal-body-description"]}>
                                <p>A software developer with a passion for automation and orchestration.</p>
                                <p><span>Title:</span> Full-Stack Software Engineer</p>
                                <p><span>Coding Experience:</span> 10+ years</p>
                                <p><span>Passions:</span> Python, Rust, MicroServices</p>
                            </div>
                        </div>
                        <div class={styles["window-cursor"]}>
                            <span class="i-cursor-indicator">></span>
                            <span class="i-cursor-underscore">_</span>
                        </div>
                    </main>
                </div>
            </section>
        </>
    );
    }
);
