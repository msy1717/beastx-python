# Contributing to BeastX

Thank you for your interest in contributing to BeastX! 🎉

## Maintainer

- **GitHub**: [@msy1717](https://github.com/msy1717)
- **Telegram**: [@GodmrunaL](https://t.me/GodmrunaL)

## How to Contribute

### 1. Report Bugs

Found a bug? Please report it!

- **Check existing issues**: [GitHub Issues](https://github.com/msy1717/beastx-python/issues)
- **Create new issue**: Include description, steps to reproduce, expected vs actual behavior
- **Contact directly**: Telegram [@GodmrunaL](https://t.me/GodmrunaL)

### 2. Suggest Features

Have an idea for improvement?

- Open a feature request on GitHub Issues
- Discuss on Telegram with the maintainer
- Explain the use case and benefits

### 3. Submit Code

Want to contribute code?

#### Setting Up Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/msy1717/beastx-python.git
cd beastx-python

# Install in development mode
pip install -e .[dev]

# Install dependencies
pip install -r requirements.txt
```

#### Code Guidelines

- **Follow PEP 8**: Python style guide
- **Add docstrings**: Document all functions and classes
- **Write tests**: Add tests for new features
- **Keep API compatible**: Maintain Telethon-like API structure
- **Update docs**: Document changes in docs/

#### Commit Guidelines

```bash
# Good commit messages
git commit -m "Add file upload functionality to client"
git commit -m "Fix session encryption bug"
git commit -m "Update documentation for events"

# Not so good
git commit -m "fixes"
git commit -m "update"
```

#### Pull Request Process

1. Create a feature branch: `git checkout -b feature-name`
2. Make your changes
3. Test thoroughly
4. Update documentation
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

### 4. Improve Documentation

Documentation contributions are always welcome!

- Fix typos or unclear explanations
- Add examples
- Improve API reference
- Translate to other languages

### 5. Help Others

- Answer questions in GitHub Issues
- Help users on Telegram
- Share your BeastX projects
- Write tutorials or blog posts

## Development Priorities

### High Priority
1. **MTProto Implementation**: Core protocol functionality
2. **Authentication**: User and bot login
3. **Message Operations**: Send, receive, edit, delete
4. **Update Handling**: Real-time updates

### Medium Priority
1. **File Operations**: Upload and download
2. **Media Handling**: Photos, videos, documents
3. **Advanced Events**: All event types
4. **Session Management**: Multiple sessions, encryption

### Low Priority
1. **CLI Tools**: Command-line utilities
2. **Performance Optimization**: Speed improvements
3. **Additional Features**: Nice-to-have functionality

## Using Telethon as Reference

When implementing features, use **Telethon** as your primary reference:

- **Repository**: https://github.com/LonamiWebs/Telethon
- **Documentation**: https://docs.telethon.dev/

See [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) for detailed guidance.

## Code of Conduct

### Be Respectful
- Respect all contributors
- Be constructive in feedback
- Welcome newcomers
- Credit others' work

### Be Professional
- Keep discussions focused
- Avoid personal attacks
- Don't spam or post off-topic content

### Give Credit
- Always acknowledge Telethon's inspiration
- Credit contributors for their work
- Reference sources when using code

## Testing

Before submitting:

```bash
# Run tests (when implemented)
pytest tests/

# Check code style
black beastx/
flake8 beastx/

# Build documentation
mkdocs build
```

## Documentation

Update documentation for any changes:

```bash
# Serve docs locally
mkdocs serve

# View at http://localhost:8000
```

## Questions?

- **GitHub Issues**: Ask questions there
- **Telegram**: [@GodmrunaL](https://t.me/GodmrunaL)
- **Email**: Check setup.py for maintainer email

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Acknowledgments

**Special Thanks to:**
- **Telethon** and Lonami Exo for the amazing API design
- **All contributors** who help improve BeastX
- **The Telegram team** for the platform and API

---

Thank you for contributing to BeastX! 💜

**Maintainer**: [@msy1717](https://github.com/msy1717) | **Telegram**: [@GodmrunaL](https://t.me/GodmrunaL)
