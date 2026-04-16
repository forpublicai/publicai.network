---
title: Cursor Demo - AI Coding in Slack
layout: page
nav_title: Cursor Demo
description: Learn how to use Cursor AI (Kilo) in Slack for automated code generation, testing, and deployment.
---

## What is Cursor?

**Cursor** is an AI-powered coding assistant that can autonomously handle complex software development tasks. Through its **Kilo** agent system, Cursor can work in the background on multi-step projects, from creating new features to fixing bugs to deploying changes.

When integrated with Slack, Cursor becomes a collaborative team member that can:
- Generate complete features from simple descriptions
- Fix bugs and refactor code
- Write and run tests
- Create and merge pull requests
- Deploy changes to production

This demo page itself was created by Cursor! 🤖

## How to Use Cursor in Slack

### Basic Workflow

Using Cursor in Slack is as simple as mentioning it with your request:

```
@Cursor [your task description]
```

**Example:**
```
@Cursor Create a new landing page for our product with a hero section, 
features grid, and call-to-action buttons. Match our existing design system.
```

### Step-by-Step Instructions

#### 1. **Mention @Cursor in a Slack channel**

Tag `@Cursor` (or `@Kilo` if configured) in any message where you want AI assistance with a coding task.

#### 2. **Provide clear task description**

Be specific about what you want. Good requests include:
- **What** you want to build or change
- **Where** it should go (file paths, repo names)
- **Context** about your tech stack or requirements
- **Constraints** like styling guidelines or dependencies

#### 3. **Cursor works autonomously**

The agent will:
- Explore your codebase to understand the structure
- Plan the implementation approach
- Write the necessary code
- Run tests if configured
- Commit changes to a new branch
- Push to your repository

#### 4. **Review and merge**

Cursor will report back with:
- Summary of changes made
- Branch name and PR link
- Any issues encountered
- Next steps for review

You can then review the PR and merge it yourself, or ask Cursor to handle the merge if it has appropriate permissions.

## Best Practices

### ✅ Do's

**Be Specific**
```
@Cursor Add a dark mode toggle to the settings page. 
Use our existing theme system and save preference to localStorage.
```

**Provide Context**
```
@Cursor Fix the memory leak in the UserService. 
We're seeing issues when users navigate between pages frequently.
```

**Reference Files or Sections**
```
@Cursor Refactor the authentication logic in src/auth/
to use our new OAuth provider.
```

**Specify the Repository**
```
@Cursor In the forpublicai/publicai.network repo, 
create a contributors page showing team members.
```

### ❌ Don'ts

**Too Vague**
```
@Cursor Make the app better
```

**Missing Context**
```
@Cursor Fix the bug
```
(Which bug? Where?)

**Multiple Unrelated Tasks**
```
@Cursor Add dark mode, refactor the database layer, 
update dependencies, and redesign the homepage
```
(Break into separate requests)

## Example Use Cases

### Creating New Features

```
@Cursor Create an API endpoint at /api/events that returns 
upcoming events from our database. Include pagination and 
filtering by date range.
```

### Bug Fixes

```
@Cursor The login form on mobile isn't validating email 
addresses correctly. Fix the validation logic and add tests.
```

### Documentation

```
@Cursor Generate API documentation for all endpoints in 
src/api/ using JSDoc format. Include request/response examples.
```

### Refactoring

```
@Cursor Refactor the UserProfile component to use React hooks 
instead of class components. Maintain all existing functionality.
```

### Testing & Deployment

```
@Cursor Add unit tests for the PaymentService class. 
Aim for >80% code coverage and test edge cases.
```

## Advanced Features

### Multi-Step Projects

Cursor excels at complex, multi-step tasks:

```
@Cursor Build a complete user authentication system:
1. Create login/signup pages
2. Implement JWT token handling
3. Add password reset flow
4. Create protected route middleware
5. Add role-based access control
```

### Working Across Multiple Files

Cursor can coordinate changes across your entire codebase:

```
@Cursor Rename the User model to Account throughout 
the application. Update all imports, tests, and documentation.
```

### Environment Setup

If Cursor encounters missing dependencies, it will attempt to install them automatically. For complex setups, you can run an environment configuration agent to prepare your project.

## Tips for Success

1. **Start Small**: Test Cursor with simple tasks before delegating complex features
2. **Review Output**: Always review the generated code and test thoroughly
3. **Iterate**: Provide feedback if the result isn't quite right
4. **Use Branches**: Cursor automatically creates branches for safety
5. **Check CI/CD**: Ensure your automated tests catch any issues
6. **Provide Examples**: Link to similar existing code when helpful

## Under the Hood

When you mention Cursor in Slack:

1. **Request Processing**: Your message is analyzed to understand the task
2. **Repository Access**: Cursor clones and explores your repository
3. **Planning**: The agent creates a task breakdown and implementation plan
4. **Implementation**: Code is written, following your project's patterns
5. **Testing**: Changes are validated (if tests are configured)
6. **Version Control**: Changes are committed with descriptive messages
7. **Push & PR**: Code is pushed to a new branch and ready for review

## Getting Started

Ready to try Cursor yourself?

1. **Ensure Cursor has access** to your repositories and Slack workspace
2. **Tag @Cursor** with a small test task to get familiar
3. **Review the results** and provide feedback
4. **Scale up** to more complex tasks as you build confidence

[Join the Public AI Network Slack](mailto:hello@publicai.network){:target="_blank" rel="noopener" class="button"}

## Questions?

- **Can Cursor access private repos?** Yes, with appropriate permissions configured
- **What languages does it support?** All major programming languages and frameworks
- **How much does it cost?** Contact Cursor for pricing information
- **Can it make mistakes?** Yes! Always review generated code before merging
- **What if I need help?** Tag @Cursor again with follow-up questions or corrections

## Learn More

- [Public AI Network Homepage](/)
- [Seminar Series](/seminar)
- [Contributing](/contributing/)
- [Publications](/publications)

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
    border-left: 3px solid #EF233C;
    padding: 15px;
    overflow-x: auto;
    border-radius: 3px;
}

.page-content pre code {
    background: none;
    padding: 0;
}

.page-content ul li {
    margin-bottom: 8px;
}

.page-content blockquote {
    background: #f0f0f0;
    border-left: 4px solid #EF233C;
    padding: 15px 20px;
    margin: 20px 0;
}
</style>

*This page was autonomously created by Cursor AI as a demonstration of its capabilities.*
