export async function fetchJson(path, options = {}) {
  const response = await fetch(path, {
    headers: {
      Accept: 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Request failed for ${path}: ${response.status}`);
  }

  return response.json();
}

export function getResumeData() {
  return fetchJson('/api/v1/resume');
}

export function getGithubUser() {
  return fetchJson('/api/v1/github/user');
}
