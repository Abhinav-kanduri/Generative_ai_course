# Main Branch Protection Setup

**Author:** Abhinav Kanduri  
**GitHub:** @Abhinav-kanduri  
**LinkedIn:** https://www.linkedin.com/in/abhinav-kanduri-a943b9353/  
**Purpose:** Knowledge transfer only.

## Course Navigation

- [Course home](README.md)
- [Foundation Week 1 dashboard](Foundation_week1/README.md)
- [Foundation Week 1 overview](Foundation_week1/Topics_covered.md)
- [Machine Learning algorithms](Foundation_week1/Machine_Learning_Algorithms.md)
- [Natural Language Processing techniques](Foundation_week1/Natural_Language_Processing_Techniques.md)
- [Deep Learning algorithms](Foundation_week1/Deep_Learning_Algorithms.md)
- [Transformer architecture](Foundation_week1/Transformer_Architecture_End_to_End.md)
- [Transformer model families](Foundation_week1/Transformer_Model_Families.md)

GitHub branch protection is controlled in the repository settings, not only by files in the repository.

Use these settings to make sure no one can directly change the `main` branch except you as the repository admin.

## 1. Update CODEOWNERS

Open this file:

```text
.github/CODEOWNERS
```

The CODEOWNERS file is already configured with:

```text
* @Abhinav-kanduri
```

## 2. Enable GitHub Pages

In GitHub:

1. Go to repository **Settings**.
2. Open **Pages**.
3. Under **Build and deployment**, select **GitHub Actions**.
4. Save the setting.

The workflow file is:

```text
.github/workflows/deploy.yml
```

It deploys the course notes when changes are pushed to `main`.

## 3. Protect the Main Branch

In GitHub:

1. Go to repository **Settings**.
2. Open **Branches**.
3. Select **Add branch protection rule**.
4. Set branch name pattern:

```text
main
```

Enable these options:

- Require a pull request before merging.
- Require approvals.
- Require review from Code Owners.
- Dismiss stale pull request approvals when new commits are pushed.
- Require status checks to pass before merging, if you add tests later.
- Require conversation resolution before merging.
- Do not allow bypassing the above settings unless you intentionally want admins to bypass.
- Restrict who can push to matching branches.

For **Restrict who can push to matching branches**, add only your GitHub user.

## 4. Recommended Admin Setting

If you want absolutely no direct changes to `main`, even by admins, enable:

```text
Do not allow bypassing the above settings
```

If you want yourself as admin to be able to make emergency changes, leave admin bypass allowed, but restrict push access to only your GitHub username.

## Important Note

The deployment workflow deploys the site.

The branch protection settings protect `main`.

Both are needed.
