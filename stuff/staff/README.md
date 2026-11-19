# Staff guide: group branches on GitHub

← Back to the [course script](../../README.md#readme)

From zero to one branch per student group. All commands go into the Ubuntu
terminal: copy with **Ctrl+Shift+C**, paste with **Ctrl+Shift+V**.

`[TODO: guide needs to be tried on Mac, Windows and Linux and adjusted accordingly]`

## 1. GitHub account

Sign up at https://github.com/signup, confirm your email, turn on two-factor
authentication (Settings → Password and authentication).
*The repository is public: your username appears next to every commit.*

## 2. Ubuntu and git

- **Linux:** nothing to do.
- **Windows:** in PowerShell as administrator run `wsl --install`, restart, open the
  "Ubuntu" app, choose a username and password. From now on, work only there.

```bash
git --version
```
*Prints a version number. If "command not found": `sudo apt install git`.*

## 3. Write access

Send your GitHub username to Joel and accept the invitation (email, or
https://github.com/TizzuLab/Blockrophage/invitations).
*Anyone can read the repository; creating branches needs Write access.*

## 4. Who you are

```bash
git config --global user.name "First Last"
git config --global user.email "ID+username@users.noreply.github.com"
```
*Every commit carries this name and email. Take the private address from GitHub →
Settings → Emails, so your real email stays out of the public repository.*

## 5. SSH key

```bash
ssh-keygen -t ed25519 -C "ID+username@users.noreply.github.com"
cat ~/.ssh/id_ed25519.pub
```
Press Enter at every question. Paste the printed line into GitHub → Settings → SSH
and GPG keys → New SSH key. Then:
```bash
ssh -T git@github.com
```
*Must answer "Hi USERNAME!" with the account that accepted the invitation.*

## 6. Clone

```bash
cd ~
git clone git@github.com:TizzuLab/Blockrophage.git
cd Blockrophage
```
*Copies the repository to `~/Blockrophage`.*

## 7. Claude Code (optional helper)

An AI assistant in the terminal that runs the next steps with you, explains each
command and asks before it changes anything on GitHub.
```bash
curl -fsSL https://claude.ai/install.sh | bash
cd ~/Blockrophage
claude
```
*The first start opens a browser to sign in with a Claude account.
`[TODO: which account the staff use, ask Joel]` Start it from inside `~/Blockrophage`:
it then reads the repository's rules in `CLAUDE.md`. Ask in plain words, e.g.
"create the group branches as in stuff/staff/README.md, step by step". Leave with
`/exit`.*

## 8. Create the group branches

```bash
git fetch origin
for g in a b c d; do
  git branch 2027/group-$g origin/dev
  git push -u origin 2027/group-$g
done
```
*One branch per group, named by year and group (script, Section 3), each starting
from the current `dev`. Change `a b c d` to the number of groups.*
`[TODO: confirm with Joel whether group branches start from dev or main]`

Check:
```bash
git branch -r
```
*`origin/2027/group-a` to `-d` must be listed; they also appear in the branch
dropdown on github.com.*

## 9. Students

Joel gives each student Write access; the student then switches to their group's
branch, in RStudio or with `git switch 2027/group-a`.
*Students never create branches. Branch rules with the supervisor as reviewer are set
by Joel on github.com.*

## If something goes wrong

| Message | Meaning and fix |
|---|---|
| `cd: no such file or directory` | The folder does not exist: clone first, or check capital letters. |
| `Permission ... denied to NAME` | NAME has no Write access: accept the invitation, or check that NAME is your account. |
| `Permission denied (publickey)` | SSH key not on GitHub: repeat step 5. |
| `repository rule violations` | A rule blocks this branch name: ask Joel. |
| `a branch named ... already exists` | It is already on your computer: `git push -u origin 2027/group-X`. |
| `claude: command not found` | Close and reopen the terminal after the install. |
