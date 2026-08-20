---
title: "Using the SSH protocol to connect from DataHub to GitHub"
format:
  html:
    theme: cosmo
    css: ../styles.css
    toc: true
    code-copy: true
    code-block-background: true
execute:
  freeze: auto
---

One can also use the SSH protocol to interact with GitHub, rather than HTTPS, as we have been doing.

When cloning a repository, it would look like this (note `git@github.com:` instead of `https://github.com/`):

```bash
git clone git@github.com:<your_username>/newton-practice.git
```

Then for authentication, you would set up an SSH key pair with:

- one file containing the private key that is kept in the `.ssh` subdirectory of your home directory on your computer (your DataHub instance in this case), and
- one file containing the public key that is also in the `.ssh` subdirectory from which you will copy the contents to [your GitHub account](https://github.com/settings/keys) by clicking on `New SSH key` via the green button in the upper right.

Software Carpentry has [detailed instructions](https://swcarpentry.github.io/git-novice/07-github.html)

If you run `ssh -T git@github.com` you'll be able to verify if you've set things up correctly.

Note that if you initially set up your local repository to use HTTPS, you'll need to reconfigure things to use SSH. You can run this:

```bash
git remote set-url origin git@github.com:<your_username>/newton-practice.git
```

Then to verify the change:

```bash
git remote -v
```

and you should see "git" rather than "https" in the result.
