---
title: Contributing to Public AI Network
layout: page
nav_title: Contributing
description: Everyone is welcome to contribute to publicai.network - no permission needed!
---

## Welcome Contributors! 

**You don't need to ask permission to contribute to this site.** Anyone can open a **pull request** (a proposed change) to make improvements or additions to publicai.network. We actively encourage it!

Whether you want to:
- Fix a typo
- Add an event
- Update contributor information
- Improve documentation
- Add a new page
- Suggest design improvements

**Just open a PR!** We're excited to see your contributions.

## New to This? Technical Terms Explained

Don't worry if you're not familiar with the technical terms below. You can contribute in many ways, and we'll help you learn!

**Common Terms:**
- **PR (Pull Request)**: A proposed change to the website. Think of it like suggesting an edit to a shared document - someone reviews it, and if it looks good, they accept it and your changes go live.
- **Repository (or "repo")**: The folder containing all the website's files and code, stored on GitHub.
- **GitHub**: A website where code and projects are stored and shared, making it easy for people to collaborate.
- **Fork**: Making your own copy of the repository so you can experiment with changes without affecting the original.
- **Branch**: A separate version of the website where you can make changes. Like working on a draft before publishing.
- **Commit**: Saving your changes with a description of what you changed. Like saving a document with a note about your edits.
- **Merge**: Accepting a pull request and adding those changes to the main website.
- **Markdown**: A simple way to format text (like making something **bold** or creating lists) using plain text. Much easier than HTML!
- **Jekyll**: The software that turns our simple text files into a full website.

**Don't let the terminology intimidate you!** You can contribute by simply describing what you want changed, and our Slack bot or community members will handle the technical parts.

## Why Contribute?

The Public AI Network is a community effort to build AI as public infrastructure. This website is itself a public resource, and we believe it should be as open and collaborative as the movement it represents.

Your contributions help:
- Keep information accurate and up-to-date
- Share knowledge with the broader community
- Make public AI resources more accessible
- Strengthen the movement for public AI

## How to Contribute

### 1. **Direct GitHub Contribution**

The traditional way - make your own copy, edit it, and propose your changes:

1. Visit the [publicai.network repository](https://github.com/forpublicai/publicai.network) (the folder with all our website files)
2. Click "Fork" to make your own copy
3. Make your changes to the files
4. Submit a pull request (your proposed changes)
5. Wait for review and feedback

**Tech Details** (for those interested):
- This is a Jekyll site (static site generator) built with Markdown (simple text formatting)
- Pages are `.md` files in the root or subdirectories
- Navigation menu is configured in `_config.yml`
- Styling/design is in `assets/css/` and `_sass/`

### 2. **Use the Slack Bot** (Recommended!)

We have AI-powered infrastructure to make contributing even easier:

**In our Slack workspace, just type:**

```
@Cursor [describe the change you want to make]
```

**Examples:**

```
@Cursor Add my name to the contributors page. 
I'm Sarah Chen from MIT, focused on AI safety and public interest tech.
```

```
@Cursor Update the upcoming events section to include 
the Public AI meetup on March 25th in Berlin.
```

```
@Cursor Fix the broken link on the libraries page 
- it should point to https://example.com
```

The Slack bot will:
- Understand your request
- Make the necessary code changes
- Create a branch and open a PR
- Report back with a link to review

**You can even ask Cursor to merge changes directly** by pinging someone with write access (see below).

### 3. **Issue a Request**

Not comfortable with code? No problem:

- Open a [GitHub Issue](https://github.com/forpublicai/publicai.network/issues) describing what you'd like changed
- Send a message in Slack with your suggestion
- Email us at [hello@publicai.network](mailto:hello@publicai.network)

Someone from the community will help make it happen.

## What Happens After You Submit?

### Review Process

All contributions go through a quick review process:

1. **Automated Checks**: Basic tests run automatically (making sure nothing breaks)
2. **Community Review**: Someone with edit access will review your proposed changes
3. **Feedback & Discussion**: We may suggest improvements or ask questions
4. **Merge**: Once approved, your changes are added to the live website!

**Review time**: Most contributions are reviewed within 1-3 days.

### Getting Edit Access

Regular contributors can get direct edit access to the website, which allows you to:
- Review and approve other people's proposed changes
- Make changes directly without waiting for approval
- Help maintain and improve the site

**To get edit access:**
- Contribute a few successful changes to show you understand the project
- Let us know you're interested in becoming a regular maintainer
- We'll add you to the team!

It's an informal process - we trust our community.

## Quick Approvals via Slack

**Have an urgent fix or update?**

If you need something approved and published quickly, you can ping one of our regular contributors with edit access in Slack:

**People who can approve changes:**
- Joshua Tan (`@Joshua Tan`)
- Sam Klein (`@Sam Klein`)
- Nick Garcia (`@Nick Garcia`)
- B Cavello (`@B Cavello`)
- Brandon Jackson (`@Brandon Jackson`)

Just mention them along with your proposed changes link or change request, and they can help get it live faster.

**Example:**
```
@Joshua Tan Could you review and approve this change? 
It updates the seminar date that was incorrect.
[link to your proposed changes]
```

## Types of Contributions We Love

### Content Updates

- **Events**: Add upcoming events or update past events
- **Contributors**: Add yourself or update your information
- **Publications**: Link to new papers or resources
- **News**: Add recent developments in public AI

### Improvements

- **Bug Fixes**: Broken links, typos, formatting issues
- **Accessibility**: Making the site more accessible
- **Performance**: Optimizations and improvements
- **Documentation**: Clarifying instructions or processes

### New Features

- **New Pages**: Educational content, guides, resources
- **Design Enhancements**: Visual improvements (please discuss first)
- **Functionality**: New features or tools (please discuss first)

**For larger changes**, we recommend opening an issue or posting in Slack first to discuss the approach.

## Contribution Guidelines

To keep things smooth:

### Content Standards

- **Accuracy**: Ensure information is correct and sourced
- **Tone**: Match the welcoming, professional tone of the site
- **Relevance**: Keep content aligned with public AI themes
- **Neutrality**: Present information objectively

### Technical Standards

- **Markdown**: Use proper Markdown syntax
- **Links**: Test that all links work
- **Formatting**: Match existing formatting conventions
- **Mobile**: Consider mobile users (the site is responsive)

### Code of Conduct

- Be respectful and collaborative
- Assume good intentions
- Welcome newcomers
- Focus on what's best for the community
- Give credit where credit is due

## Example Contributions

### Adding Yourself to Contributors

1. Edit the `contributors.md` file
2. Add a new card in the appropriate alphabetical section
3. Follow the existing card format (copy and modify an existing one)
4. Submit your proposed change with the title: "Add [Your Name] to contributors"

### Adding an Event

1. Edit `index.md` (the homepage file)
2. Add a row to the "Upcoming events" table
3. Include date, event name, and location
4. Submit your proposed change with title: "Add [Event Name] to events"

### Fixing a Typo

1. Find and edit the file with the typo
2. Make the correction
3. Submit your proposed change with title: "Fix typo on [page name]"

**Pro tip**: For simple fixes, you can edit directly on GitHub's web interface without downloading anything!

## Need Help?

**Never contributed to a website or open source project before?**

That's completely okay! We're happy to help you get started. Many of our contributors were beginners when they started.

**Get help:**
- **Slack**: Ask questions in `#general` or `#website` - our community is friendly!
- **Email**: [hello@publicai.network](mailto:hello@publicai.network)
- **GitHub Guides**: [How to propose a change](https://docs.github.com/en/pull-requests) (if you want to learn the technical details)

**Not technical? No problem!** Just describe what you want changed in Slack or via email, and someone will help make it happen. You don't need to understand code to contribute ideas and content.

Don't be shy - we were all beginners once, and we want to make this as accessible as possible.

## Recognition

All contributors are:
- Listed in the git commit history
- Welcome to add themselves to the contributors page
- Invited to join our Slack community
- Part of the Public AI Network movement

**Thank you for helping build public AI!**

---

## Quick Links

- [GitHub Repository](https://github.com/forpublicai/publicai.network)
- [Open Issues](https://github.com/forpublicai/publicai.network/issues)
- [Contributors Page](/contributors)
- [Join our Slack](mailto:hello@publicai.network)
- [Newsletter Signup](https://publicai.substack.com)

---

<style>
.page-content h2 {
    margin-top: 40px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
}

.page-content h3 {
    margin-top: 25px;
    color: #333;
}

.page-content code {
    background: #f5f5f5;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
}

.page-content pre {
    background: #f8f8f8;
    border-left: 3px solid #667eea;
    padding: 15px;
    overflow-x: auto;
    border-radius: 3px;
    margin: 15px 0;
}

.page-content pre code {
    background: none;
    padding: 0;
}

.page-content blockquote {
    background: #f0f4ff;
    border-left: 4px solid #667eea;
    padding: 15px 20px;
    margin: 20px 0;
    font-style: normal;
}

.page-content ul li {
    margin-bottom: 8px;
}

.page-content strong {
    color: #333;
}

/* Highlight boxes */
.page-content h2::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 20px;
    background: #667eea;
    margin-right: 10px;
    vertical-align: middle;
}
</style>

<div style="text-align: center; margin: 50px 0 20px 0; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <h2 style="color: white; border: none; margin: 0; padding: 0;">Ready to Contribute?</h2>
  <p style="margin: 15px 0; font-size: 18px;">Propose a change today - no permission needed!</p>
  <a href="https://github.com/forpublicai/publicai.network" style="display: inline-block; padding: 12px 30px; background: white; color: #667eea; text-decoration: none; border-radius: 25px; font-weight: bold; margin-top: 10px;">View on GitHub →</a>
</div>

*This page was created to encourage open collaboration and make contributing as easy as possible. Have suggestions for improving this guide? Propose a change!*
