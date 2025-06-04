"""Utility functions for Visual Novel Script Creator and data processing."""

from typing import Dict, List, Any, Optional
import json
import pandas as pd
import numpy as np
from datetime import datetime


# Original template functions (preserved)
def get_sample_data(rows: int = 10) -> pd.DataFrame:
    """Generate sample data for demonstration.

    Args:
        rows: Number of rows to generate, defaults to 10

    Returns:
        DataFrame with sample data including random numbers and dates
    """
    np.random.seed(42)  # For reproducibility

    return pd.DataFrame(
        {
            "date": pd.date_range(start="2024-01-01", periods=rows),
            "value_a": np.random.randn(rows),
            "value_b": np.random.randn(rows),
            "category": np.random.choice(["A", "B", "C"], size=rows),
        }
    )


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process input dataframe by adding computed columns.

    Args:
        df: Input DataFrame that should contain 'value_a' and 'value_b' columns

    Returns:
        DataFrame with additional computed columns
    """
    # Create a copy to avoid modifying the input
    processed = df.copy()

    # Add some computed columns if the required columns exist
    if "value_a" in processed.columns and "value_b" in processed.columns:
        processed["sum"] = processed["value_a"] + processed["value_b"]
        processed["mean"] = (processed["value_a"] + processed["value_b"]) / 2
        processed["abs_diff"] = abs(processed["value_a"] - processed["value_b"])

    return processed


def validate_dataframe(
    df: pd.DataFrame, required_columns: Optional[list[str]] = None
) -> bool:
    """Validate that a DataFrame meets the required schema.

    Args:
        df: DataFrame to validate
        required_columns: List of column names that must be present

    Returns:
        True if validation passes, raises ValueError otherwise
    """
    if required_columns is None:
        required_columns = ["value_a", "value_b"]

    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"DataFrame is missing required columns: {', '.join(missing_cols)}"
        )

    return True


# Visual Novel Script Creator functions
def create_character(
    name: str,
    role: str,
    age: int,
    personality: str,
    background: str,
    goals: str
) -> Dict[str, Any]:
    """Create a character dictionary with all necessary information.
    
    Args:
        name: Character's name
        role: Character's role in the story
        age: Character's age
        personality: Personality traits description
        background: Character's background story
        goals: Character's goals and motivations
        
    Returns:
        Dictionary containing character information
    """
    return {
        'name': name,
        'role': role,
        'age': age,
        'personality': personality,
        'background': background,
        'goals': goals,
        'created_at': datetime.now().isoformat()
    }


def create_story_arc(
    name: str,
    description: str,
    start_chapter: int,
    end_chapter: int,
    themes: str,
    characters: List[str]
) -> Dict[str, Any]:
    """Create a story arc dictionary.
    
    Args:
        name: Arc name
        description: Arc description
        start_chapter: Starting chapter number
        end_chapter: Ending chapter number
        themes: Main themes of the arc
        characters: List of character names involved
        
    Returns:
        Dictionary containing story arc information
    """
    return {
        'name': name,
        'description': description,
        'start_chapter': start_chapter,
        'end_chapter': end_chapter,
        'themes': themes,
        'characters': characters,
        'created_at': datetime.now().isoformat()
    }


def create_milestone(
    name: str,
    description: str,
    chapter: int,
    milestone_type: str,
    impact: str,
    related_arc: Optional[str] = None
) -> Dict[str, Any]:
    """Create a story milestone dictionary.
    
    Args:
        name: Milestone name
        description: Milestone description
        chapter: Chapter where milestone occurs
        milestone_type: Type of milestone
        impact: Impact level of the milestone
        related_arc: Related story arc (optional)
        
    Returns:
        Dictionary containing milestone information
    """
    return {
        'name': name,
        'description': description,
        'chapter': chapter,
        'type': milestone_type,
        'impact': impact,
        'related_arc': related_arc,
        'created_at': datetime.now().isoformat()
    }


def generate_dialogue_options(
    character_name: str,
    situation: str,
    personality_traits: str
) -> List[str]:
    """Generate dialogue options based on character and situation.
    
    Args:
        character_name: Name of the speaking character
        situation: Current situation/context
        personality_traits: Character's personality traits
        
    Returns:
        List of potential dialogue options
    """
    # This is a simplified version - in a real app you might use AI/ML here
    base_options = [
        f"What should we do about {situation}?",
        f"I think we need to consider our options here.",
        f"This reminds me of something that happened before.",
        f"Let's approach this carefully."
    ]
    
    # Modify based on personality (simplified logic)
    if 'confident' in personality_traits.lower():
        base_options.append(f"I know exactly what to do in this situation!")
    if 'shy' in personality_traits.lower():
        base_options.append(f"Um... maybe we should think about this more?")
    if 'aggressive' in personality_traits.lower():
        base_options.append(f"We need to take action now!")
    
    return base_options[:4]  # Return up to 4 options


def export_script_format(
    story_concept: str,
    characters: List[Dict[str, Any]],
    story_arcs: List[Dict[str, Any]],
    milestones: List[Dict[str, Any]],
    dialogue_scenes: List[Dict[str, Any]],
    format_type: str
) -> str:
    """Export the visual novel script in specified format.
    
    Args:
        story_concept: The main story concept
        characters: List of character dictionaries
        story_arcs: List of story arc dictionaries
        milestones: List of milestone dictionaries
        dialogue_scenes: List of dialogue scene dictionaries
        format_type: Export format ("JSON", "Markdown", "CSV Summary")
        
    Returns:
        Formatted export string
    """
    export_data = {
        'story_concept': story_concept,
        'characters': characters,
        'story_arcs': story_arcs,
        'milestones': milestones,
        'dialogue_scenes': dialogue_scenes,
        'export_date': datetime.now().isoformat()
    }
    
    if format_type == "JSON":
        return json.dumps(export_data, indent=2)
    
    elif format_type == "Markdown":
        return generate_markdown_export(export_data)
    
    elif format_type == "CSV Summary":
        return generate_csv_summary(export_data)
    
    else:
        return json.dumps(export_data, indent=2)


def generate_markdown_export(data: Dict[str, Any]) -> str:
    """Generate a Markdown format export of the visual novel script.
    
    Args:
        data: Dictionary containing all script data
        
    Returns:
        Markdown formatted string
    """
    md_content = []
    
    # Title and concept
    md_content.append("# Visual Novel Script")
    md_content.append(f"\n**Export Date:** {data['export_date']}")
    md_content.append("\n## Story Concept")
    md_content.append(f"\n{data['story_concept']}")
    
    # Characters
    if data['characters']:
        md_content.append("\n## Characters")
        for char in data['characters']:
            md_content.append(f"\n### {char['name']} ({char['role']})")
            md_content.append(f"- **Age:** {char['age']}")
            md_content.append(f"- **Personality:** {char['personality']}")
            md_content.append(f"- **Background:** {char['background']}")
            md_content.append(f"- **Goals:** {char['goals']}")
    
    # Story Arcs
    if data['story_arcs']:
        md_content.append("\n## Story Arcs")
        for arc in data['story_arcs']:
            md_content.append(f"\n### {arc['name']}")
            md_content.append(f"**Chapters:** {arc['start_chapter']} - {arc['end_chapter']}")
            md_content.append(f"**Description:** {arc['description']}")
            md_content.append(f"**Themes:** {arc['themes']}")
            if arc['characters']:
                md_content.append(f"**Characters:** {', '.join(arc['characters'])}")
    
    # Milestones
    if data['milestones']:
        md_content.append("\n## Story Milestones")
        sorted_milestones = sorted(data['milestones'], key=lambda x: x['chapter'])
        for milestone in sorted_milestones:
            md_content.append(f"\n### Chapter {milestone['chapter']}: {milestone['name']}")
            md_content.append(f"**Type:** {milestone['type']}")
            md_content.append(f"**Impact:** {milestone['impact']}")
            md_content.append(f"**Description:** {milestone['description']}")
            if milestone['related_arc']:
                md_content.append(f"**Related Arc:** {milestone['related_arc']}")
    
    # Dialogue Scenes
    if data['dialogue_scenes']:
        md_content.append("\n## Dialogue Scenes")
        for scene in data['dialogue_scenes']:
            md_content.append(f"\n### {scene['name']} (Chapter {scene['chapter']})")
            md_content.append(f"**Characters:** {', '.join(scene['characters'])}")
            md_content.append(f"**Dialogue:** {scene['dialogue']}")
            if scene['branches']:
                md_content.append("**Response Options:**")
                for i, branch in enumerate(scene['branches'], 1):
                    md_content.append(f"{i}. {branch}")
    
    return "\n".join(md_content)


def generate_csv_summary(data: Dict[str, Any]) -> str:
    """Generate a CSV summary of the visual novel script.
    
    Args:
        data: Dictionary containing all script data
        
    Returns:
        CSV formatted string
    """
    # Create summary statistics
    summary_data = {
        'Metric': [
            'Total Characters',
            'Total Story Arcs',
            'Total Milestones',
            'Total Dialogue Scenes',
            'Estimated Chapters',
            'Main Characters',
            'Supporting Characters'
        ],
        'Count': [
            len(data['characters']),
            len(data['story_arcs']),
            len(data['milestones']),
            len(data['dialogue_scenes']),
            max([m['chapter'] for m in data['milestones']] + [0]) if data['milestones'] else 0,
            len([c for c in data['characters'] if c['role'] == 'Main Character']),
            len([c for c in data['characters'] if c['role'] not in ['Main Character', 'Love Interest']])
        ]
    }
    
    df = pd.DataFrame(summary_data)
    return df.to_csv(index=False)


def analyze_story_structure(
    characters: List[Dict[str, Any]],
    story_arcs: List[Dict[str, Any]],
    milestones: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Analyze the story structure and provide insights.
    
    Args:
        characters: List of character dictionaries
        story_arcs: List of story arc dictionaries
        milestones: List of milestone dictionaries
        
    Returns:
        Dictionary containing analysis results
    """
    analysis = {
        'character_count': len(characters),
        'arc_count': len(story_arcs),
        'milestone_count': len(milestones),
        'estimated_length': 0,
        'character_roles': {},
        'pacing_analysis': []
    }
    
    # Character role distribution
    for char in characters:
        role = char['role']
        analysis['character_roles'][role] = analysis['character_roles'].get(role, 0) + 1
    
    # Estimate story length
    if milestones:
        analysis['estimated_length'] = max(m['chapter'] for m in milestones)
    elif story_arcs:
        analysis['estimated_length'] = max(arc['end_chapter'] for arc in story_arcs)
    
    # Basic pacing analysis
    if milestones:
        milestone_chapters = [m['chapter'] for m in milestones]
        milestone_chapters.sort()
        
        for i in range(len(milestone_chapters) - 1):
            gap = milestone_chapters[i + 1] - milestone_chapters[i]
            if gap > 3:
                analysis['pacing_analysis'].append(f"Large gap between chapters {milestone_chapters[i]} and {milestone_chapters[i + 1]}")
    
    return analysis


def validate_story_structure(
    characters: List[Dict[str, Any]],
    story_arcs: List[Dict[str, Any]],
    milestones: List[Dict[str, Any]]
) -> List[str]:
    """Validate the story structure and return warnings/suggestions.
    
    Args:
        characters: List of character dictionaries
        story_arcs: List of story arc dictionaries
        milestones: List of milestone dictionaries
        
    Returns:
        List of validation messages
    """
    warnings = []
    
    # Check for main character
    main_chars = [c for c in characters if c['role'] == 'Main Character']
    if len(main_chars) == 0:
        warnings.append("Consider adding a Main Character to your story.")
    elif len(main_chars) > 3:
        warnings.append("You have many Main Characters - consider if some should be Supporting characters.")
    
    # Check story arc coverage
    if story_arcs:
        total_chapters = max(arc['end_chapter'] for arc in story_arcs) if story_arcs else 0
        covered_chapters = set()
        for arc in story_arcs:
            covered_chapters.update(range(arc['start_chapter'], arc['end_chapter'] + 1))
        
        if len(covered_chapters) < total_chapters:
            warnings.append("Some chapters may not be covered by any story arc.")
    
    # Check milestone distribution
    if milestones and len(milestones) > 0:
        milestone_impacts = [m['impact'] for m in milestones]
        if milestone_impacts.count('Critical') > 3:
            warnings.append("You have many Critical milestones - consider varying the impact levels.")
        if 'High' not in milestone_impacts and 'Critical' not in milestone_impacts:
            warnings.append("Consider adding some High or Critical impact milestones for dramatic tension.")
    
    return warnings