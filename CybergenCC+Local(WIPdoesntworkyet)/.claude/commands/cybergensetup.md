# /cybergensetup - Initialize Cybergenic Framework

Initialize the complete Cybergenic Framework by running the setup script.

## What This Does

Executes the `setup_cybergenic.py` Python script which automatically creates all necessary directories, files, agent definitions, and configurations for the Cybergenic Framework.

## Usage

```bash
/cybergensetup
```

## Implementation

Run the setup script:

```bash
python setup_cybergenic.py
```

The script will:
- Check dependencies (Python 3.8+, psutil)
- Create directory structure (.cybergenic/, .claude/, seed/, framework/, output/)
- Create tracking files (counters, JSON state files)
- Create 11 agent definitions:
  - 1 Architect (Sonnet 4.5)
  - 1 Coordinator (Sonnet 4.5)
  - 8 Specialized Synthesizers (Haiku 4)
  - 1 Chaperone (Haiku 4)
- Create MCP configuration (.claude/mcp.json)
- Initialize git repository
- Create seed template (seed/requirements.md)
- Display setup summary

## Agent Definitions Created

The setup creates specialized synthesizers for each capability type:

1. **architect.md** - Creates DNA.md with Sacred Rules (Sonnet 4.5)
2. **coordinator.md** - Transcribes DNA→RNA and routes to specialized synthesizers (Sonnet 4.5)
3. **synthesizer_transform.md** - Synthesizes data transformation proteins (Haiku 4)
4. **synthesizer_validate.md** - Synthesizes data validation proteins (Haiku 4)
5. **synthesizer_manage_state.md** - Synthesizes state management proteins (Haiku 4)
6. **synthesizer_coordinate.md** - Synthesizes coordination proteins (Haiku 4)
7. **synthesizer_communicate.md** - Synthesizes external I/O proteins (Haiku 4)
8. **synthesizer_monitor.md** - Synthesizes monitoring proteins (Haiku 4)
9. **synthesizer_decide.md** - Synthesizes decision-making proteins (Haiku 4)
10. **synthesizer_adapt.md** - Synthesizes interface adaptation proteins (Haiku 4)
11. **chaperone.md** - Validates protein folding (Haiku 4)

Each specialized synthesizer is optimized for its specific capability type with domain-specific best practices and patterns.

## Next Steps

After setup completes:
1. Edit `seed/requirements.md` with your project description
2. Run `/cybergenrun` to begin conception (creates DNA.md via Architect)
3. Continue evolution with additional `/cybergenrun` calls
4. The Coordinator will automatically route proteins to the appropriate specialized synthesizer

See the script's output for detailed information about what was created.
