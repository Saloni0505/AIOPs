from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="How to Pull the Main Branch from Git", ln=True, align='C')
pdf.ln(10)

pdf.cell(200, 10, txt="This guide explains the steps to pull the main branch from a Git repository.", ln=True)
pdf.ln(5)

pdf.cell(200, 10, txt="1. Navigate to your repository directory:", ln=True)
pdf.cell(200, 10, txt="   cd /path/to/your/repository", ln=True)
pdf.ln(5)

pdf.cell(200, 10, txt="2. Check the current branch and status:", ln=True)
pdf.cell(200, 10, txt="   git status", ln=True)
pdf.cell(200, 10, txt="   - This shows your current branch and any changes.", ln=True)
pdf.ln(5)

pdf.cell(200, 10, txt="3. Fetch the latest changes from the remote repository:", ln=True)
pdf.cell(200, 10, txt="   git fetch origin", ln=True)
pdf.cell(200, 10, txt="   - 'origin' is the default remote name. Replace if different.", ln=True)
pdf.cell(200, 10, txt="   - This downloads updates without merging.", ln=True)
pdf.ln(5)

pdf.cell(200, 10, txt="4. Switch to the main branch:", ln=True)
pdf.cell(200, 10, txt="   git checkout main", ln=True)
pdf.cell(200, 10, txt="   - If main doesn't exist locally, use: git checkout -b main origin/main", ln=True)
pdf.cell(200, 10, txt="   - This creates and switches to main if needed.", ln=True)
pdf.ln(5)

pdf.cell(200, 10, txt="5. Pull the latest changes into the main branch:", ln=True)
pdf.cell(200, 10, txt="   git pull origin main", ln=True)
pdf.cell(200, 10, txt="   - This fetches and merges changes from origin/main.", ln=True)
pdf.cell(200, 10, txt="   - If already on main, 'git pull' suffices if tracking is set.", ln=True)
pdf.ln(5)

pdf.cell(200, 10, txt="6. Verify the pull:", ln=True)
pdf.cell(200, 10, txt="   git log --oneline -5", ln=True)
pdf.cell(200, 10, txt="   - Check recent commits to confirm updates.", ln=True)
pdf.ln(10)

pdf.cell(200, 10, txt="Notes:", ln=True)
pdf.cell(200, 10, txt="- Ensure Git is installed and configured.", ln=True)
pdf.cell(200, 10, txt="- Handle merge conflicts if they arise during pull.", ln=True)
pdf.cell(200, 10, txt="- Use 'git branch -a' to list all branches.", ln=True)

pdf.output("git_pull_main.pdf")